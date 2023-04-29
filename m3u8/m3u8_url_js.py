import re
import requests
from crypto.Cipher import AES
import threading

#m3u8视频js逆向爬虫
# 随便找一个浏览器头部信息
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

# 控制台network搜索m3u8,提取m3u8列表地址
url_1 = "https://pri-cdn-tx.xiaoeknow.com/appcugpcu9l7438/private_index/1664508907Ci9NRq.m3u8?sign=2d4cf6cf6e448437d7d633e1c4a96faa&t=64340ab8"


url_text=requests.get(url=url_1,headers=headers).text#获取其中的文本信息
url_text=url_text.strip()#去除换行避免出错
print(url_text)
# file = open ( file=r"D:\uu.txt", mode="a", encoding="utf8" )
# file.write ( url_text )


key_url=re.findall('URI="(.*?)"',url_text,re.S)[0]# 正则匹配URI

# 控制台源代码搜索‘xe.basic-platform.material-center.distribute.vod.pri.get’找到后面的window.USERID
# 去控制台打印window.USERID逆向uid
# key_url=f"{key_url}&uid=u_anonymous_643398cc0754c_H6725SOhFx"

print(key_url)
key=requests.get(url="https://gitcode.net/weixin_38503250/index/-/raw/master/2095da82b67988a18a3049b29f49eeee.key?inline=false,headers=headers").content

print(key)
print(list(key))
print(len(key))