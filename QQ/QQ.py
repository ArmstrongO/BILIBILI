import requests
import re

user_input = input ( "请输入需要查询的QQ或者是手机号：" )

def cha_ele():
    url=f"https://zy.xywlapi.cc/qqphone?phone={user_input}"
    res=requests.get(url=url)
    return res.text

def cha_qq():
    url = f"https://zy.xywlapi.cc/qqapi?qq={user_input}"
    res=requests.get(url=url)
    return res.text

def run():
    if user_input.isdigit():
        if re.match ( r'^1[3456789]\d{9}$', user_input ):
            print(cha_ele())
            pass
        else:
            print(cha_qq())
            pass
    else:
        print("输入错误")
        pass
if __name__ ==  "__main__":
    run()