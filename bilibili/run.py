import math
import random
import time
import uuid
import requests
import re
import json


def get_tunnel_proxies():
    proxy_host="tunne12.qg.net:17955"
    proxy_username="xx"
    proxy_pwd="xx"

    return {
        "http": "http://{}:{}@{}".format(proxy_username,proxy_pwd,proxy_host),
        "https": "http://{}:{}@{}".format(proxy_username,proxy_pwd,proxy_host)
    }

def gen_uuid():
    uuid_sec=str(uuid.uuid4())
    time_sec=str(int(time.time()*1000 % 1e5))
    time_sec=time_sec.rjust(5,"0")

    return "{}{}infoc".format(uuid_sec.time_sec)

def gen_b_lsid():
    data = ""
    for i in range(8):
        v1=math.ceil(16*random.uniform((0,1)))
        v2=hex(v1)[2:].upper()
        data+=v2
    result=data.rjust(8,'0')

    e=int(time.time()*1000)
    t=hex(e)[2:].upper()

    b_lsid="{}_{}".format(result,t)
    return b_lsid

def play(video_url,proxies):
    bvid=video_url.rsplit("/")[-1]
    session =requests.session()
    session.proxies=proxies
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/B08C390B"

    })
    res=session.get(video_url)


def get_video_id_info(video_url,proxies):
    session=requests.session()
    bvid = video_url.rsplit ( "/" )[-1]
    res=session.get(
        url="https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp".format(bvid),
        proxies=proxies
    )

    cid=res.json()['data'][0]['cid']
    res=session.get(
        url="https://api.bilibili.com/x/web-interface/view?cid={}&bvid={}".format ( cid,bvid ),
        proxies=proxies
    )
    res_json=res.json()
    aid=res_json['data']['aid']
    view_count=res_json['data']['stat']['view']


