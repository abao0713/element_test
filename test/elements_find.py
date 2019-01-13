#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
#等待10s
driver.implicitly_wait(10)
#示例代码地址
driver.get("file:///C:/Users/Administrator/Desktop/elements_find.html")
#定位复选框并选择
try:
    checkboxes = driver.find_elements_by_tag_name("control-group")
    # 选择所有的checkbox并全部勾上
    for box in checkboxes:
        box.click()
except Exception as e:
    print("Exception found", format(e))


# 选择页面上所有的input，只勾选输入类型为checkbox的选项框
try:
    inputs = driver.find_elements_by_tag_name('input')
    for input in inputs:
        if input.get_attribute('type') == 'checkbox':
            input.click()
except Exception as e:
    print("Exception found", format(e))

time.sleep(2)
#退出浏览器
driver.quit()
