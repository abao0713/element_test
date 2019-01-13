<html>
 <head></head>
 <body>
  <form id="form" class="fm" name="f">
    　　
   <span id="s_kw_wrap" class="btn_wr s_btn_wr bg"> 　　　　
        <input id="TANGRAM__PSP_10__userName" type="text" name="userName" class="pass-text-input pass-text-input-userName open" autocomplete="off" value="" placeholder="手机/邮箱/用户名" xpath="1" /> 　　</span> 　　
   <span id="s_kw_wrap" class="btn_wr s_btn_wr bg"> 　　　　
        <input id="su" class="btn self-btn bg s_btn" type="submit" value="百度一下" />
            <select id="sur" class="btn self-btn bg s_btn">
                <option>北极</option>
                <option>南美</option>
                <option>华南</option>
                <option>欧洲</option>
        </select> 　
    </span>
  </form>
 </body>
</html>

# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")
#根据常用属性进行定位
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__userName']")
driver.find_element_by_xpath("//*[@name='userName']")
#根据其它属性进行定位
driver.find_element_by_xpath("//*[@type='submit']")
#定位时加入html标签
driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_10__userName']")
#通过父级元素进行定位
driver.find_element_by_xpath("//span[@id='s_kw_wrap']/input")
#通过高层级定位
driver.find_element_by_xpath("//form[@id='form']/span/input")
#通过索引进行定位"北极"，注意索引从1开始
driver.find_element_by_xpath("//*[@id='sur']/option[1]")
driver.find_element_by_xpath("input")
driver.find_element_by_xpath("input")




time.sleep(2)
driver.quit()
