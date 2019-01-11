<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off" xpath="1">





# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")
# 找到百度首页底部的百度前必读然后点击

driver.find_element_by_css_selector("input")#根据tag_name

driver.find_element_by_css_selector("#kw")#根据id方式
driver.find_element_by_css_selector("input#kw")#增加tag_name加上id的方式

driver.find_element_by_css_selector(".s_ipt")#根据class_name的方式
driver.find_element_by_css_selector("*.s_ipt")
driver.find_element_by_css_selector("input.s_ipt")#根据tag_name加上class_name的方式
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")




time.sleep(2)
driver.quit()














