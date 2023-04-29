# 单层网站爬v1.0-1

import time
import urllib.request
import re
import requests

# urll = f"http://www.y54f.buzz/AAtupian/AAAtb/asia/"  # 要爬取的url
# url = "http://tfapi.top/API/nypic.php"  #获取url
# http://www.886hh.buzz/AAtupian/AAAtb/meitui/

# /AAtupian/AAAtb/meitui/index-2.html

  # 要爬取的url
def cc_sese():
    urll = f"https://www.444ggf.com/htm/2022/12/8/meituisiwa/561383.html"
    tiqu_lianjie = 'https://www.y21j45k89b66.com/160C08/'  # 目标地址前缀
    pat = f'{tiqu_lianjie}(.*?).jpg'  # 正则匹配以PNG结尾的地址
    data = urllib.request.urlopen ( urll ).read ().decode ( "utf-8" )  # 读取网页的内容并解码
    time.sleep ( 2 )
    relut = re.compile ( pat ).findall ( data )  # 会返回一个列表
    file = open ( r"C:\Users\Administrator\Desktop\1\mimi99.txt", "a", encoding="utf-8" )  # 这里我定义了一个自己的存储路径，大家可以根据自己的路径修改
    for ii in relut:
        # url=f'https://www.444ggf.com/{tiqu_lianjie}{ii}.html'
        # tiqu_lianjiee = 'https://www.y21j45k89b66.com/'
        # pat = f'{tiqu_lianjiee}(.*?)jpg'
        # data = urllib.request.urlopen ( url ).read ().decode ( "utf-8" )  # 读取网页的内容并解码
        # time.sleep ( 2 )
        # relut = re.compile ( pat ).findall ( data )  # 会返回一个列表
        # file = open ( r"C:\Users\Administrator\Desktop\1\sese99.txt", "a", encoding="utf-8" )
        # for i in relut:
        file.write ( f'{tiqu_lianjie}' )  # 先写进开头
        file.write ( ii )  # 将提取的内容写入文件
        file.write ( "jpg" )  # 将格式写入
        file.write ( "\n" )  # 表示换行
        print('0000')
    print ( "end" )


# y = 1
# for n in range ( 1, 150 ):
#     urll = f"https://www.444ggf.com/meituisiwa/list_{y}.html"
#     y+=1
#     time.sleep(1)
#     cc_sese()
#     print ( "endend" )
# time.sleep(55)

def www():
    urll = f"http://www.y54f.buzz/AAtupian/AAAtb/meitui/"
    # 获取urlhttp://www.y54f.buzz/AAtupian/AAAwz/173071.html
    tiqu_lianjiee = '/AAtupian/AAAwz/'
    patt = f'{tiqu_lianjiee}(.*?)html'
    dataa = urllib.request.urlopen ( urll ).read ().decode ( "utf-8" )  # 读取网页的内容并解码
    relutt = re.compile ( patt ).findall ( dataa )  # 会返回一个列表
    for ii in relutt:
        url = f"http://www.y54f.buzz{tiqu_lianjiee}{ii}html"
        print ( url )  # https://wo-ai-tutu.com/时间/20170818/977/5536.jpg
        tiqu_lianjie = 'https://wo-ai-tutu.com/'
        pat = f'{tiqu_lianjie}(.*?)jpg'
        data = urllib.request.urlopen ( url ).read ().decode ( "utf-8" )  # 读取网页的内容并解码
        relut = re.compile ( pat ).findall ( data )  # 会返回一个列表
        file = open ( r"C:\Users\Administrator\Desktop\1\sese6.txt", "a", encoding="utf-8" )
        # 这里我定义了一个自己的存储路径，大家可以根据自己的路径修改
        for i in relut:
            file.write ( f'{tiqu_lianjie}' )  # 先写进开头
            file.write ( i )  # 将提取的内容写入文件
            file.write ( "jpg" )  # 将格式写入
            file.write ( "\n" )  # 表示换行
    print ( "end" )


# for n in range ( 1, 30 ):
#     time.sleep ( 1 )
#     y+=1
#     cc()
#     print ( "end2" )


# patt = '(.*?)jpg'
# string = 'test1.jpg abcd test2.jpg efgh test3.jpg ijkl'
#
# matches = re.findall(patt, string)
# for match in matches:
#     cc()
# http://www.886hh.buzz/AAtupian/AAAwz/118581.html
# https://wo-ai-tutu.com/shunv/20170818/621/1153.jpg
# https://wo-ai-tutu.com/shunv/20170818/656/944.jpg
# https://wo-ai-tutu.com//meitui/20201108/771/156662.jpg
# https: // wo - ai - tutu.com / shunv / 20170818 / 621 / 1154.jpg

def get_default_address():
    res = requests.get ( url=f"https://space.bilibili.com/36047134/channel/seriesdetail?sid=333090" )#f"http://tfapi.top/API/nypic.php"
    res=res.text
    print ( res )


get_default_address()