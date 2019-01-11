#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
#等待10s
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#定位百度输入框并输入文本“书语湘镡”
try:
    driver.find_element_by_id("kw").send_keys("书语湘镡")
    driver.find_element_by_id("su").click()
except Exception as e:
    print("Exception found", format(e))

time.sleep(2)
#退出浏览器
driver.quit()
