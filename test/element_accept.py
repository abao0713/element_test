
#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
#等待10s
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
# 定位到输入框，从而获得获得输入框尺寸
size = driver.find_element_by_id("kw").size
#定位到输入框按钮并且获取按钮上的文本
text = driver.find_element_by_css_selector("input[type='submit']").text
#返回元素的属性值，可以是id、name、type 或元素拥有的其它任意属性
attribute = driver.find_element_by_id("kw").get_attribute('type')
#返回元素的css属性值
css_attribute = driver.find_element_by_id("kw").value_of_css_property("font-size")
#返回元素的结果是否可见，返回结果为True 或False
result = driver.find_element_by_css_selector("input[type='submit']").is_displayed()
time.sleep(2)
driver.quit()