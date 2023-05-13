import threading
import requests
import time
import queue
import re

start = time.time()
# 填充队列
URLs = {
    '111.16.50.12': '9002',
    '58.20.184.187': '9091',
    '121.196.120.232': '9999',
    '117.94.120.236': '9000'
}


# 为线程定义一个函数
class myThread(threading.Thread):
    # 定义线程
    def __init__(self, name, q):
        threading.Thread.__init__(self)
        # 线程名称
        self.name = name
        #
        self.q = q

    def run(self):
        # 开始线程
        print("Starting " + self.name)
        while True:
            try:
                # 执行crawl耗时操作
                crawl(self.name, self.q)
            except:
                break
        # 退出线程
        print("Exiting " + self.name)


def getHTMLText(url, data, headers, proxies, code='utf-8'):
    try:
        r = requests.get(url=url, params=data, headers=headers, proxies=proxies)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return "GET异常"


def parse(html):
    # 利用正则表达式 解析并获取页面中所有IP地址
    ip_list = re.findall(
        r'(?<![\.\d])(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])',
        html)
    return ip_list


def crawl(threadNmae, q):
    ip = q.get(timeout=2)
    print(threadNmae + '开始测试' + str(ip) + '...')
    url = 'http://httpbin.org/ip'
    proxies = {"http": f"http://{ip}:{URLs.get(ip)}", "https": f"http://{ip}:{URLs.get(ip)}"}
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }
    html = getHTMLText(url=url, headers=headers, data=None, proxies=proxies)
    if html == "GET异常":
        print(str(ip) + '无效')
        return False

    if parse(html)[0] == ip:
        print(str(ip) + '有效')
    else:
        print(str(ip) + '无效')
        URLs.pop(ip)
    return parse(html)[0] == ip

workQueue = queue.Queue(len(URLs.keys()))
for url in URLs.keys():
    workQueue.put(url)

threads = []
for i in range(1, 5):
    # 创建4个新线程
    thread = myThread("Thread-" + str(i), q=workQueue)
    # 开启新线程
    thread.start()
    # 添加新线程到线程列表
    threads.append(thread)

# 等待所有线程完成
for thread in threads:
    thread.join()

end = time.time()
print("Queue多线程IP验证耗时：{} s".format(end - start))
print("Exiting Main Thread")

