# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang

import time
from selenium import webdriver

start_url = "https://www.baidu.com/"
driver = webdriver.Chrome()
driver.get(url=start_url)

html = driver.page_source
print(html)
time.sleep(1)
driver.close()
