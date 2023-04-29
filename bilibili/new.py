import requests
import json
import re
res=requests.get("https://www.bilibili.com/video/BV1Vs4y1m7P9")
date_list=re.findall(r'INITIAL_STATE__=(.+);\(function',res.text)
date_lis1=re.findall(r'视频播放量(.+);、弹幕量',res.text)
date_dict=json.loads(date_list[0])
# print(date_lis1)
aid=date_dict["aid"]
cid=date_dict['videoData']['cid']
view_count=date_dict['stat']['view']
# print(res.m3u8)
print(view_count)
# print(cid)