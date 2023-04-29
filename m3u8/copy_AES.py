import re
import requests
import os, uuid
from crypto.Cipher import AES


class Demo ( object ):
    '''
        调用方法：
        1、先实例化一个Demo对象
        2、把提取的m3u8url放在url, 把提取的ts  url前缀放在base_url
        2、调用demo的download_ts方法,并将两个参数（url,base_url）传进去

        只需要在download方法中传入一个m3u8url即可
    '''

    # 返回当前文件路径
    def get_filpath(self):
        # 先判断ts_files文件夹是否存在，不存在则创建
        if not os.path.exists ( 'ts_files' ):
            os.system ( 'mkdir ts_files' )
        f_path = os.getcwd () + '\\ts_files\\'
        return f_path

    # 将ts文件合并转换成mp4
    def ts_to_mp4(self):
        path = self.get_filpath ()
        mp4_name = str ( uuid.uuid1 () ) + '.mp4'
        print ( mp4_name )
        merge_cmd = 'copy /b ' + path + '\*.ts ' + path + '\\' + mp4_name
        #  转换成功后，删除ts文件
        # del_cmd = 'del ' + path + '\*.ts'

        os.system ( merge_cmd )
        # os.system(del_cmd)
        print ( '转换完成' )

    def download_ts(self, url, base_url):
        # 获取初始的ts_urls 和content
        res = requests.get ( url=url )
        pay_list = res.text.split ( '\n' )
        ts_urls = pay_list[9:-1:3]

        # 获取加密的方法和密钥
        content = res.text
        method = re.findall ( '#EXT-X-KEY:METHOD=(.*?),', content )[0]
        # 获取加密url
        key = re.findall ( '#EXT-X-KEY:METHOD=AES-128,(.*?)\n', content )[0]
        key_url = re.findall ( '"(.*?)"', key )[0]
        # 对加密url发起请求
        res = requests.get ( key_url )
        # 获取返回来的加密密钥
        key = res.content
        # 获取偏移向量 iv
        iv = re.findall ( 'IV=(.*?)\n', content )[0]
        iv = iv.replace ( '0x', '' )

    iv = bytes.fromhex ( iv )
    cryptor = AES.new ( key, AES.MODE_CBC, iv )

    for i, p in enumerate ( ts_urls ):
        ts_url = base_url + p
        res = requests.get ( ts_url )
        '''
        注意：ts文件名，要按001这种形式命令，不然，等下在window下合并顺序会出现错乱，导致视频无法播放
        　　　ts文件比较多的，可以添加位数 如，0001,00001等
             rjust(3,'0'),3表示位数
        '''
        file_name = str ( i ).rjust ( 3, '0' ) + '.ts'
        file = self.get_filpath () + file_name
        with open ( file, 'wb' ) as f:
            # 对ts文件内容进行解密
            f.write ( cryptor.decrypt ( res.content ) )
            print ( '下载完成' )
    self.ts_to_mp4 ()


if __name__ == '__main__':
    # url为第一步提取的url
    url = 'https://1258712167.vod2.myqcloud.com/5a81e359vodtranssh1258712167/fe20c2755285890815554519079/drm/voddrm.token.dWluPTM1MTc4MzU1NDQ7c2tleT1AQklIMFlFYU9SO3Bza2V5PUpPUE44RVUtLXdMUWxqeERZVHUyNEFoa3kqVGh5NGp5clBpbUIzbUJscW9fO3Bsc2tleT0wMDA0MDAwMDc2MTNiOTRmMjA4NmU1NTJjNzhkYzI3NzdhYjQ3NGQxYzZhNGEzN2ZkNTVmMDc4ODZhODFjNDI3MTBmZTA2MTJmN2EwZjFkNzczOTU1OTMyO2V4dD07dWlkX3R5cGU9MDt1aWRfb3JpZ2luX3VpZF90eXBlPTA7Y2lkPTMzODU0OTE7dGVybV9pZD0xMDM1MTg0OTg7dm9kX3R5cGU9MA==.v.f30742.m3u8?exper=0&sign=4142361e5f70dc1887bb4374a6c8499a&t=60eab641&us=6759179987002315823'
    # base_url 为第二步提取的url前缀
    base_url = 'https://1258712167.vod2.myqcloud.com/5a81e359vodtranssh1258712167/fe20c2755285890815554519079/drm/'
    h = Demo ()
    h.download_ts ( url=url, base_url=base_url )

