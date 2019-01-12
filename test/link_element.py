# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")
# 找到百度首页底部的百度前必读然后点击
try:
    driver.find_element_by_partial_link_text("百度前必读").click()

except Exception as e:
    print("Exception found", format(e))
time.sleep(2)
driver.quit()
