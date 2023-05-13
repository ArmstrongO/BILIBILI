import requests

# proxies = {
#     "http": "http://60.12.168.114:9002/",
#     "https": "https://60.12.168.114:9002",
# }
# resp = requests.get ( "https://ip.cn/api/index?ip=&type=0", proxies=proxies )
# print ( resp.text )


def getHTMLText(url, data, headers, proxies, code='utf-8'):
    try:
        # headers 避免被检测出自身为程序访问 将自己伪装成浏览器
        r = requests.get(url=url, params=data, headers=headers, proxies=proxies)
        # t = random.randint(1, 5)  # 随机睡眠 降低机器辩认度
        # time.sleep(t)
        r.raise_for_status()
        r.encoding = code
        return r.text
    # 返回静态源码或异常提示
    except:
        return "GET异常"


def test(ip, port):
    # 如果代理成功 则页面解析获取的IP应当与输入IP相同
    # True 代理成功 False代理失败
    print('开始测试' + str(ip) + '...')
    # url = 'http://httpbin.org/ip'
    url='https://api.ipify.org'
    proxies = {"http": f"http://{ip}:{port}", "https": f"http://{ip}:{port}"}
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }
    html = getHTMLText(url=url, headers=headers, data=None, proxies=proxies)
    if html == "GET异常":
        return False
