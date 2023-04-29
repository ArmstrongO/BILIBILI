import requests
import base64


def get_key_from_url(url: str, userid: str) -> str:
    """
    通过请求m3u8文件中的key的url,获取解密视频key的base64字符串密钥
    :param url: m3u8文件中获取key的url
    :param userid: 用户id，放视频时飘动的那一串
    :return: key的base64字符串
    """
    # url拼接uid参数
    url += f'&uid={userid}'
    # 发送get请求
    rsp = requests.get ( url=url )
    rsp_data = rsp.content
    if len ( rsp_data ) == 16:
        userid_bytes = bytes ( userid.encode ( encoding='utf-8' ) )
        result_list = []
        for index in range ( 0, len ( rsp_data ) ):
            result_list.append (
                rsp_data[index] ^ userid_bytes[index] )
        print ( result_list )
        return base64.b64encode ( bytes ( result_list ) ).decode ()
    else:
        print ( f"获取异常，请求返回值：{rsp.text}" )
        return ''


# https://pri-cdn-tx.xiaoeknow.com/appcugpcu9l7438/private_index/1664508907Ci9NRq.m3u8?sign=168254ad995149bdb047c4977ba76105&t=64341d7a
if __name__ == '__main__':
    _url='https://v.tedu.cn/p/t_pc/course_pc_detail/video/v_612cee33e4b092ac9838d54a?product_id=p_61287ef5e4b092ac9837981c&content_app_id=&type=6'
    # _url = 'https://app.xiaoe-tech.com/xe.basic-platform.material-center.distribute.vod.pri.get/1.0.0?app_id=app****3&mid=m_G****t_3****H&urld=e****f9'
    _uid = 'u_5****f_o****5'
    base64_key = get_key_from_url ( url=_url, userid=_uid )
    print ( base64_key )