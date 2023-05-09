

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Administrator\Desktop\1\chromedriver.exe")

# driver.get("https://www.baidu.com")
#
# driver.maximize_window()
# for n in range ( 1, 5):
#     driver.find_element(By.ID,"kw").send_keys(f"GPT{n}")
#     driver.find_element(By.ID,"su").click()
#     # driver.find_element(By.ID,"u").click()
#     time.sleep(4)
#     driver.find_element(By.CLASS_NAME,"toindex").click()

pre_dir = r'D:/temp/scrapy/'
# driver = webdriver.Chrome('./driver/chromedriver.exe')
# 设置超时时间 10s
driver.set_page_load_timeout(10)
url_str = f"https://cdfdf3dsdsnf0jssdfadfadfuio90.dyp007.com/art/chapter/id/72/page/5.html"
driver.get(url_str)
page_source = driver.page_source
file_path = r'D:/22.html'
with open(file_path,'w',encoding='utf-8') as fw:
    fw.write(page_source)
driver.close()
driver.quit()


from selenium import webdriver

# 启动Chrome浏览器
# driver = webdriver.Chrome('chromedriver.exe')

# 打开百度网页
driver.get('https://cdfdf3dsdsnf0jssdfadfadfuio90.dyp007.com/art/chapter/id/72/page/5.html')

elements = driver.find_elements_by_css_selector(".fixed.promptBox")
driver.execute_script("arguments[0].parentNode.removeChild(arguments[0]);")

time.sleep(33)
# driver.quit()