# from time import sleep
import time

# import selenium
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
def yiyan():
    url = "https://v1.hitokoto.cn/"
    params = {
        "c": "f",
        "encode": "text"
    }
    try:
        res = requests.get(url, params=params)
        res.raise_for_status()  # 抛出异常
    except requests.exceptions.RequestException as e:
        print("网络连接出现问题: ", e)
        return None
    else:
        return res.text

def cnode():
    global wc
    wc=webdriver.Chrome(r"C:\Users\Administrator\Desktop\1\chromedriver.exe")
    wc.get("http://119.91.224.105:3000")
    time.sleep ( 1 )
    wc.maximize_window()

def login():
    wc.find_element(By.CSS_SELECTOR,"body > div.navbar > div > div > ul > li:nth-child(6) > a").click()
    wc.find_element(By.ID,"name").send_keys("test_lz")
    time.sleep(1)
    wc.find_element(By.ID,"pass").send_keys("123456")
    time.sleep(1)
    wc.find_element(By.CSS_SELECTOR,"#signin_form > div.form-actions > input").click()
    time.sleep(3)

def fabu():
    wc.find_element(By.CLASS_NAME,"brand").click()
    time.sleep ( 3 )
    wc.find_element(By.CSS_SELECTOR,"#create_topic_btn > span").click()
    time.sleep(1)
    wc.find_element(By.CSS_SELECTOR,"#create_topic_form > fieldset > span.tab-selector").click()
    wc.find_element ( By.CSS_SELECTOR, "#tab-value > option:nth-child(2)" ).click ()
    time.sleep(1)
    wc.find_element(By.ID,"title").send_keys(f"{yiyan()}")
    time.sleep(1)
    wc.find_element(By.CLASS_NAME,"CodeMirror-code").click()
    time.sleep ( 1 )
    ActionChains(wc).send_keys(f"内容:{yiyan()}").perform()
    time.sleep (2)
    js = "window.scrollTo(100,450)"
    wc.execute_script ( js )
    time.sleep (3)
    wc.find_element(By.CSS_SELECTOR,"#create_topic_form > fieldset > div > div > div.editor_buttons > input").click()
    # ActionChains(wc).key_down(7)
    time.sleep ( 2 )
    return
    # ActionChains(wc).
    # 点击发布

    # wc.find_element ( By.CLASS_NAME, "CodeMirror-code" ).send_keys("777777")
    # wc.find_element().send_keys("666666")
    # wc.find_element ( By.CSS_SELECTOR,"#create_topic_form > fieldset > div > div > div.CodeMirror.cm-s-paper > div.CodeMirror-scroll > div.CodeMirror-sizer > div > div > div > div.CodeMirror-code > pre:nth-child(2) > span.cm-strong.cm-em.cm-header" ).send_keys("7777")



cnode()
login()

while 1:
    fabu()


# sleep(3)


time.sleep(4)