# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.zhiling.robotsh.com/#/login")
# 找到输入框并输入账号密码
try:
    driver.find_element_by_css_selector("input[type='text']").clear()
    driver.find_element_by_css_selector("input[type='text']").send_keys("aybj")
    driver.find_element_by_css_selector("input[type='password']").clear()
    driver.find_element_by_css_selector("input[type='password']").send_keys("Aa123456")
    driver.find_element_by_xpath("//span[contains(text(),'登 录')]").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/div[1]").click()
    driver.find_element_by_xpath("//li[contains(text(),'当前批次')]").click()
    text = driver.find_element_by_xpath("//tbody//tr[2]//td[12]//div[1]").text
    print(text)
except Exception as e:
    print("Exception found", format(e))
time.sleep(2)
driver.quit()
