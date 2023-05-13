import requests



url = 'https://www.lvlv.asia'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.33'
}

try:
    res = requests.get ( url, headers=headers )
    if res.headers.get ( 'content-type' ) == 'application/json':# 如果返回的响应数据为JSON格式，则可以使用res.json()方法获取其内容
        print ( res.json ()["message"] )
    else:
        # 否则用res.text获取响应数据
        print ( res.text )

    res.raise_for_status ()  # 抛出异常

except requests.exceptions.RequestException as e:
    print ( "网络连接出现问题: ", e )
