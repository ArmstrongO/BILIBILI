import requests
import time
import threading #si'ruai'di
#
# ip='121.196.120.232'
# port='3129'




def yiyi():
    # url = 'https://api.ipify.org'
    # url = 'http://httpbin.org/ip'
    url ='https://ip.cn/api/index?ip=&type=0'
    proxies = {"http": f"http://{ip}:{port}", "https": f"http://{ip}:{port}"}
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }
    try:
        res = requests.get(url, headers=headers, data=None, proxies=proxies)
        res.raise_for_status()  # 抛出异常
    except requests.exceptions.RequestException as e:
        print("网络连接出现问题: ", e)
        return None
    else:
        # print(res.text)
        return res.text




with open( 'IP_Pool1.txt', 'r' ) as file:
    for line in file:
        # 去除空白字符并分割IP地址和端口号
        ip, port = line.strip().split(',')
        port = port.strip()  # 去除端口号的空格
        # print(f"ip = {ip}, port = {port}")
        # print(ip)
        # print(port)
        url = 'https://ip.cn/api/index?ip=&type=0'
        proxies = {"http": f"http://{ip}:{port}", "https": f"http://{ip}:{port}"}
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
        }
        try:
            res = requests.get ( url, headers=headers, data=None, proxies=proxies )
            res.raise_for_status ()  # 抛出异常
        except requests.exceptions.RequestException as e:
            print ( "网络连接出现问题: ", e )
            print ( f"ip = {ip}, port = {port}" )
        else:
            # print(res.text)
            pass
