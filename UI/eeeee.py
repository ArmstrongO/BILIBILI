from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 无头模式
browser = webdriver.Chrome(options=chrome_options)

def check_element(xpath):
    try:
        element = browser.find_element(By.XPATH, xpath)
        return element
    except NoSuchElementException:
        return None

while True:
    # 等待用户输入
    time.sleep(20)
    element = check_element('//*[@class="fixed promptBox"]')
    if element:
        print("找到元素：", element)
        # 删除元素和其子元素
        browser.execute_script("arguments[0].parentNode.removeChild(arguments[0]);", element)
        print("已删除元素：", element)
    else:
        print("未找到元素")


    # 暂停5秒钟，继续检测Chrome浏览器状态
    time.sleep(5)