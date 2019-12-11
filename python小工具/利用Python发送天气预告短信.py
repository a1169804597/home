#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/7/16 22:12
#@Author :zbwu103
#@File  ：利用Python发送天气预告短信.py
#@功能：爬取中国天气网的信息通过短信的方式发送致手机

import requests
from bs4 import BeautifulSoup
#创建一个字典来存储生活指数
def shenghuozhishu():
    url="http://www.weather.com.cn/weather1d/101200101.shtml"
    response=requests.get(url)
    response.encoding=response.apparent_encoding
    html=response.text
    BS_html=BeautifulSoup(html,'lxml')
    lis=BS_html.find_all('ul',class_="clearfix")[2].find_all("li")
    zhishu={}
    i=0
    for li in lis:
        zhishu[i]=li.find("p").text
        i+=1
    return zhishu
print(shenghuozhishu())