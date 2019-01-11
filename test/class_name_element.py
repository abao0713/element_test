#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
#等待10s
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#定位百度输入框并输入文本“书语湘镡”
driver.find_element_by_class_name("s_ipt").send_keys("书语湘镡")
time.sleep(2)
#退出浏览器
driver.quit()
