#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
#等待10s
driver.implicitly_wait(10)
driver.get("https://www.126.com")
#
try:
    #由于iframe的id对象是变动的，不适宜通过id来定位到iframe
    #通过xpath定位iframe
    iframe = driver.find_element_by_xpath(".//*[@id='loginDiv' and @class='loginUrs']/iframe")
    #切换到iframe
    driver.switch_to_frame(iframe)
    #定位到iframe的登录框
    driver.find_element_by_xpath(".//*[@id='dologin']").click()
    #退出iframe，才能对iframe以外的进行定位
    driver.switch_to.default_content()
except Exception as e:
    print("Exception found", format(e))

time.sleep(2)
#退出浏览器
driver.quit()
