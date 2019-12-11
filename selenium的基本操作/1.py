#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/10/10 20:51
#@Author :zbwu103
#@File  ：1.py
#@功能：切换Frame

import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

browser=webdriver.Chrome()
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo=browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO　LOGO')
browser.switch_to.parent_frame()
logo=browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

