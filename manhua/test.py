import requests
import urllib.request
import re


#
# urll = f"https://www.444ggf.com/htm/2022/12/8/meituisiwa/561383.html"
# tiqu_lianjie = 'https://www.y21j45k89b66.com/160C08/'  # 目标地址前缀
# pat = f'{tiqu_lianjie}(.*?)//Z'  # 正则匹配以PNG结尾的地址
# data = urllib.request.urlopen ( urll ).read ().decode ( "utf-8" )  # 读取网页的内容并解码
# relut = re.compile ( pat ).findall ( data )  # 会返回一个列表
# file = open ( r"C:\mimi99.txt", "a", encoding="utf-8" )  # 这里我定义了一个自己的存储路径，大家可以根据自己的路径修改


def www():
    urll = f"https://cdfdf3dsdsnf0jssdfadfadfuio90.dyp007.com/art/chapter/id/72/page/1.html"
    tiqu_lianjiee = 'data:image/jpg;base64,/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0a%0D%0AHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIy%0D%0AMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCBBoAtADASIA%0D%0AAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQA%0D%0AAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3%0D%0AODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWm%0D%0Ap6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEA%0D%0AAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSEx%0D%0ABhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElK%0D%0AU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3%0D%0AuLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/'
    patt = f'{tiqu_lianjiee}(.*?)//Z'
    dataa = urllib.request.urlopen ( urll ).read ().decode ( "utf-8" )  # 读取网页的内容并解码
    relut = re.compile ( patt ).findall ( dataa )  # 会返回一个列表
    file = open ( r"C:\20230424.txt", "a", encoding="utf-8" )
    # for ii in relutt:
    #     url = f"http://www.y54f.buzz{tiqu_lianjiee}{ii}html"
    #     print ( url )  # https://wo-ai-tutu.com/时间/20170818/977/5536.jpg
    #     tiqu_lianjie = 'https://wo-ai-tutu.com/'
    #     pat = f'{tiqu_lianjie}(.*?)jpg'
    #     data = urllib.request.urlopen ( url ).read ().decode ( "utf-8" )  # 读取网页的内容并解码
    #     relut = re.compile ( pat ).findall ( data )  # 会返回一个列表
    #     file = open ( r"C:\20230424.txt", "a", encoding="utf-8" )
    #     # 这里我定义了一个自己的存储路径，大家可以根据自己的路径修改
    for i in relut:
        file.write ( f'{tiqu_lianjiee}' )  # 先写进开头
        file.write ( i )  # 将提取的内容写入文件
        file.write ( "//Z" )  # 将格式写入
        file.write ( "\n" )  # 表示换行
    print ( "end" )

def get_default_address():
    res = requests.get ( url=f"https://cdfdf3dsdsnf0jssdfadfadfuio90.dyp007.com/art/chapter/id/72/page/1.html" )#f"http://tfapi.top/API/nypic.php"
    res=res.text
    print ( res )


get_default_address()