

'''
def get_tunnel_proxies():
    proxy_host="tunnel6.qg.net:18964"
    proxy_username="F95CC210"
    proxy_pwd="FC72F79AAEE7"

    return {
        "http": "http://{}:{}@{}".format(proxy_username,proxy_pwd,proxy_host),
        "https": "http://{}:{}@{}".format(proxy_username,proxy_pwd,proxy_host)
    }


def get_tunnel_proxies():
    proxyAddr = "tunnel6.qg.net:18964"
    authKey = "F95CC210"
    password = "FC72F79AAEE7"
    proxyUrl = "http://%(user)s:%(password)s@%(server)s" % {
        "user": authKey,
        "password": password,
        "server": proxyAddr,
    }
    proxies = {
        "http": proxyUrl,
        "https": proxyUrl,
    }
    resp = requests.get ( "https://ip.cn/api/index?ip=&type=0", proxies=proxies )
    print ( resp.text )

'''

'''
def get_video_id_info(video_url,proxies):
    play ( video_url, proxies )
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
    duration = res_json['data']['duration']
    print ( "\n视频{}，平台播放量为:{}".format ( bvid, view_count ))
    session.close()
    return aid, bvid, cid, duration, int(view_count)


def run():
    proxies=get_tunnel_proxies()
    print(proxies)
    video_url = "https://www.bilibili.com/video/BV1bL411e7XR"
    aid, byid, cid, duration, view_count = get_video_id_info ( video_url, proxies )
    while True:
        try:
            print ( proxies )
            get_video_id_info ( video_url, proxies )
            play ( video_url, proxies )
            view_count += 1
            print ( "理论刷的播放量:",view_count)
        except Exception as e:
            pass

'''
import math
import random
import time
import uuid
import requests
import re
import json

view_count=0
def get_tunnel_proxies():
    proxyAddr = "tunnel6.qg.net:18964"
    authKey = "F95CC210"
    password = "FC72F79AAEE7"
    proxyUrl = "http://%(user)s:%(password)s@%(server)s" % {
        "user": authKey,
        "password": password,
        "server": proxyAddr,
    }
    proxies = {
        "http": proxyUrl,
        "https": proxyUrl,
    }
    resp = requests.get ( "https://ip.cn/api/index?ip=&type=0", proxies=proxies )
    print ( resp.text )
    return proxies

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
    date_list=re.findall(r'__INITIAL_STATE__=(.+);\(function',res.text)
    date_dict =json.loads(date_list[0])
    aid=date_dict['aid']
    cid=date_dict['videoData']['cid']

    _uuid=gen_uuid()
    session.cookies.set('_uuid',_uuid)

    b_lsid=gen_b_lsid()
    session.cookies.set ( 'b_lsid',b_lsid )

    session.cookies.set("CURRENT_FNVAL","4048")

    res=session.get("https://api.bilibili.com/x/frontend/finger/spi")
    buvid4 = res.json ()['data']['b_4']
    session.cookies.set ( "buvid4",buvid4)
    session.cookies.set ( "CURRENT_BLACKGAP", "8" )
    session.cookies.set ( "blackside_state", "0" )

    res = session.get (
        url='https://api.bilibili.com/x/player/v2',
        params={
            "cid": cid,
            "aid": aid,
            "bxid": bvid,
            }
    )

    ctime = int ( time.time () )
    res = session.post (
        url="https://api.bilibili.com/x/click-interface/click/web/h5",
        data={
            "aid": aid,
            "cid": cid,
            "bvid": bvid,
            "part": "1",
            "mid": "0",
            "lv": "0",
            "ftime": ctime - random.randint ( 100,500),  # 浏览器首次打开时间
            "stime": ctime,
            "jsonp": "jsonp",
            "type": "3",
            "sub_type": "0",
            "from_spmid": "",
            "auto_continued_play": "0",
            "refer_url": "",
            "bsource":"",
            "somid":""
        }
    )



def get_video_id_info(video_url, proxies):
    session=requests.session()
    bvid = video_url.rsplit ("/")[-1]
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
    duration = res_json['data']['duration']
    print ( "\n视频{}，平台播放量为:{}".format ( bvid, view_count ))
    session.close()
    return aid, bvid, cid, duration, int(view_count)


def run():
    video_url = "https://www.bilibili.com/video/BV1bL411e7XR"
    while True:
        try:
            proxies = get_tunnel_proxies()
            print(proxies)
            aid, byid, cid, duration, view_count = get_video_id_info(video_url, proxies)
            play(video_url, proxies)
            view_count += 1
            print("理论刷的播放量:", view_count)
        except Exception as e:
            print(e)
            pass

# if __name__ ==  "__main__":
#     run()

while 1:
    print(get_tunnel_proxies())