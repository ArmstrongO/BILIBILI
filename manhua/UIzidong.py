from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(r"C:\Users\Administrator\Desktop\1\chromedriver.exe")

driver.get("https://www.baidu.com")

driver.maximize_window()
for n in range ( 1, 5):
    driver.find_element(By.ID,"kw").send_keys(f"GPT{n}")
    driver.find_element(By.ID,"su").click()
    # driver.find_element(By.ID,"u").click()
    time.sleep(4)
    driver.find_element(By.CLASS_NAME,"toindex").click()

