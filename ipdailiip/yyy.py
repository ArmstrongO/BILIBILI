import random
import time
import re
from multiprocessing.dummy import Pool
import requests
from lxml import etree


# 1.获取网页静态源码的requests框架
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


# 2.代理池

# 1
def get_kuaidaili_IP():
    # 获取快代理网站前三页IP及其端口
    print('抓取快代理网站前三页IP及其端口')
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }
    parser = etree.HTMLParser(encoding="utf-8")
    ip_dic = {}

    for i in range(1, 4):
        url = 'https://free.kuaidaili.com/free/inha/' + str(i) + '/'
        html = getHTMLText(url=url, headers=headers, data=None, proxies=None)
        tree = etree.HTML(html, parser=parser)  # 加载html文件
        ip_list = tree.xpath('/html/body/div/div[4]/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/text()')
        post_list = tree.xpath('/html/body/div/div[4]/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/text()')
        dic = dict(zip(ip_list, post_list))
        ip_dic = dict(ip_dic, **dic)
    return ip_dic


# 2
def get_66ip_IP():
    # 获取66免费代理网前三页IP及其端口
    print('抓取66免费代理网前三页IP及其端口')
    ip_dic = {}
    parser = etree.HTMLParser(encoding="utf-8")
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }

    def obtain(url):
        html = getHTMLText(url=url, headers=headers, data=None, proxies=None)
        tree = etree.HTML(html, parser=parser)  # 加载html文件
        ip_list = tree.xpath('//*[@id="main"]/div[1]/div[2]/div[1]//tr/td[1]/text()')
        post_list = tree.xpath('//*[@id="main"]/div[1]/div[2]/div[1]//tr/td[2]/text()')
        dic = dict(zip(ip_list, post_list))
        return dic

    url = 'http://www.66ip.cn/index.html'
    ip_dic = dict(ip_dic, **obtain(url))
    for i in range(2, 4):
        url = 'http://www.66ip.cn/' + str(i) + '.html'
        ip_dic = dict(ip_dic, **obtain(url))

    return ip_dic


# 3
def get_ip3366_IP():
    # 获取3366云代理网站前三页IP及其端口
    print('抓取3366云代理网站前三页IP及其端口')
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }
    parser = etree.HTMLParser(encoding="utf-8")
    ip_dic = {}

    for i in range(1, 4):
        url = 'http://www.ip3366.net/free/?stype=1&page=' + str(i)
        html = getHTMLText(url=url, headers=headers, data=None, proxies=None)
        tree = etree.HTML(html, parser=parser)  # 加载html文件
        ip_list = tree.xpath('//*[@id="list"]/table/tbody/tr/td[1]/text()')
        post_list = tree.xpath('//*[@id="list"]/table/tbody/tr/td[2]/text()')
        dic = dict(zip(ip_list, post_list))
        ip_dic = dict(ip_dic, **dic)
    return ip_dic


# 4
def get_89ip_IP():
    # 获取89免费代理网站前三页IP及其端口
    print('抓取89免费代理网站前三页IP及其端口')
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }
    parser = etree.HTMLParser(encoding="utf-8")
    ip_dic = {}

    for i in range(1, 4):
        url = 'https://www.89ip.cn/index_1' + str(i) + '.html'
        html = getHTMLText(url=url, headers=headers, data=None, proxies=None)
        tree = etree.HTML(html, parser=parser)  # 加载html文件
        ip_list = tree.xpath('//div[@class="layui-form"]//tr/td[1]/text()')
        post_list = tree.xpath('//div[@class="layui-form"]//tr/td[2]/text()')
        dic = dict(zip(ip_list, post_list))
        ip_dic = dict(ip_dic, **dic)
    return ip_dic


# 5
def get_kxdaili_IP():
    # 获取云代理网站高匿与普匿两页IP及其端口
    print('抓取云代理网站高匿与普匿两页IP及其端口')
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }
    parser = etree.HTMLParser(encoding="utf-8")
    ip_dic = {}

    for i in range(1, 2):
        url = 'http://www.kxdaili.com/dailiip.html'
        html = getHTMLText(url=url, headers=headers, data=None, proxies=None)
        tree = etree.HTML(html, parser=parser)  # 加载html文件
        ip_list = tree.xpath('//div[@class="hot-product-content"]//tr/td[1]/text()')
        post_list = tree.xpath('//div[@class="hot-product-content"]//tr/td[2]/text()')
        dic = dict(zip(ip_list, post_list))
        ip_dic = dict(ip_dic, **dic)

    for i in range(1, 2):
        url = 'http://www.kxdaili.com/dailiip/2/1.html'
        html = getHTMLText(url=url, headers=headers, data=None, proxies=None)
        tree = etree.HTML(html, parser=parser)  # 加载html文件
        ip_list = tree.xpath('//div[@class="hot-product-content"]//tr/td[1]/text()')
        post_list = tree.xpath('//div[@class="hot-product-content"]//tr/td[2]/text()')
        dic = dict(zip(ip_list, post_list))
        ip_dic = dict(ip_dic, **dic)

    return ip_dic


## 3.测试

def parse(html):
    # 利用正则表达式 解析并获取页面中所有IP地址
    ip_list = re.findall(
        r'(?<![\.\d])(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)(?![\.\d])',
        html)
    return ip_list


def test(ip, port):
    # 如果代理成功 则页面解析获取的IP应当与输入IP相同
    # True 代理成功 False代理失败
    print('开始测试' + str(ip) + '...')
    url = 'http://httpbin.org/ip'
    proxies = {"http": f"http://{ip}:{port}", "https": f"http://{ip}:{port}"}
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
    }
    html = getHTMLText(url=url, headers=headers, data=None, proxies=proxies)
    if html == "GET异常":
        return False
    return parse(html)[0] == ip


def test_list(ip_dic):
    ip_list = list(ip_dic.keys())
    for num in range(len(ip_list)):
        if test(ip_list[num], ip_dic[ip_list[num]]):
            print(str(ip_list[num]) + '有效')
        else:
            print(str(ip_list[num]) + '无效')
            ip_dic.pop(ip_list[num])
    return ip_dic


## 4.结果展示
def save_ip_text(ip_dic):
    for ip in list(ip_dic.keys()):
        with open("IP_Pool1.txt", 'a', encoding='utf-8') as fd:
            fd.write(str(ip) + ",\t" + str(ip_dic[ip]) + '\n')
    print('可用IP池已保存至IP_Pool1.txt')


def show_ip(ip_dic):
    # 简单打印
    for ip in list(ip_dic.keys()):
        print(str(ip) + ":\t" + str(ip_dic[ip]))



def main():
    print('------------------------------------------------')
    print('------------------------------------------------')
    print('1.开始初步IP收集')
    ip_dic = {}
    # ip_dic = dict(ip_dic, **get_kuaidaili_IP())
    # ip_dic = dict(ip_dic, **get_66ip_IP())
    ip_dic = dict(ip_dic, **get_ip3366_IP())
    # ip_dic = dict(ip_dic, **get_89ip_IP())
    ip_dic = dict(ip_dic, **get_kxdaili_IP())
    print('2.完成初步IP收集')
    print('抓取到共计\t' + str(len(ip_dic)) + '个IP')
    print('------------------------------------------------')
    print('------------------------------------------------')
    print('3.开始可用性测试')
    print(ip_dic)
    ip_dic = test_list(ip_dic)
    print('------------------------------------------------')
    print('------------------------------------------------')
    print('4.有效IP存储')
    save_ip_text(ip_dic)
    print('最终有效IP数目计为\t' + str(len(ip_dic)))

if __name__ == '__main__':
    main()

