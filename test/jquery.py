<html>
<head>
<script type="text/javascript" src="/jquery/jquery.js"></script>
<script type="text/javascript">
$(document).ready(function(){
$("button").click(function(){
$("p").hide();
});
});
</script>
</head>

<body>
<h2>This is a heading</h2>
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
<button type="button">Click me</button>
</body>
</html>


#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
#等待10s
driver.implicitly_wait(10)
driver.get("myfile_path")
#定位按钮并点击它
input = "$('button[type='button']').click()"
driver.execute_script(input)

time.sleep(2)
#退出浏览器
driver.quit()




