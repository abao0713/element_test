<input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off" xpath="1">

<input type="submit" id="su" value="百度一下" class="bg s_btn" xpath="1">

<input id="TANGRAM__PSP_10__userName" type="text" name="userName"
class="pass-text-input pass-text-input-userName open" autocomplete="off"
value="" placeholder="手机/邮箱/用户名" xpath="1">

# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")

# tag_name方式定位
driver.find_element_by_css_selector("input")#根据tag_name
#id方式定位
driver.find_element_by_css_selector("#kw")#根据id方式
driver.find_element_by_css_selector("input#kw")#增加tag_name加上id的方式
#class_name方式定位
driver.find_element_by_css_selector(".s_ipt")#根据class_name的方式
driver.find_element_by_css_selector("*.s_ipt")
driver.find_element_by_css_selector("input.s_ipt")#根据tag_name加上class_name的方式
driver.find_element_by_css_selector("input.bg.s_btn")#class_name定位时class_name值包含空格
#其它属性定位
driver.find_element_by_css_selector("input[type='text'][name='userName']")#含有type属性和name属性
driver.find_element_by_css_selector("[type='text'][name='userName']")
#子元素路径查找法

<form id="form" class="fm" name="f">
　　<span id="s_kw_wrap" class="bg s_ipt_wr quickdelete-wrap">
　　　　<input id="TANGRAM__PSP_10__userName" type="text" name="userName"
class="pass-text-input pass-text-input-userName open" autocomplete="off"
value="" placeholder="手机/邮箱/用户名" xpath="1">
　　</span>
　　<span id="s_btn_wr" class="btn_wr s_btn_wr bg">
　　　　<input id="su" class="btn self-btn bg s_btn" type="submit" value="百度一下">
　　</span>
</form>






driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")
driver.find_element_by_css_selector("input")




time.sleep(2)
driver.quit()














