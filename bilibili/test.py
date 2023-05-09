import math
import random
import time
import uuid
import requests
import re
import json



def get_tunnel_proxies():
    proxy_host="tunnel6.qg.net:18964"
    proxy_username="F95CC210"
    proxy_pwd="FC72F79AAEE7"

    return {
        "http": "http://{}:{}@{}".format(proxy_username,proxy_pwd,proxy_host)
    }

proxies=get_tunnel_proxies()
print(proxies)