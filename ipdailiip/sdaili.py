import requests
from lxml import etree

#https://www.kuaidaili.com/free/
url = 'https://www.89ip.cn/index_1.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)



if response.status_code == 200:
    html = response.text
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser=parser)
    ip_list = tree.xpath('//div[@class="layui-form"]//tr/td[1]/text()')#layui-table
    ip_list=str(ip_list)
    port_list = tree.xpath('//div[@class="layui-form"]//tr/td[2]/text()')
    port_list=str(port_list)
    ipip = {
        ip_list: port_list
    }
    # do something with ip_list and port_list
    print(ipip)
else:
    print('Request failed with status code:', response.status_code)