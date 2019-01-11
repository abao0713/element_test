#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
#等待10s
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#定位百度首页的学术字段并点击
time.sleep(2)
driver.find_element_by_link_text("学术").click()
#driver.find_element_by_link_text(str(u"学术".encode('utf-8')))
#退出浏览器
driver.quit()
