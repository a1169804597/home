#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/5/26 21:11
#@Author :zbwu103
#@File  ：1111.py
#@功能：爬取刺激战场的步枪的属性

import requests
import json
import jsonpath
import pygal
url='https://pg.qq.com/zlkdatasys/data_zlk_zlzx.json'
response = requests.get(url)

# print(req)

req= response.json()
# print(type(req))
names=jsonpath.jsonpath(req,'$..mc_94')
# print(names)
names[1:11]
xn = jsonpath.jsonpath(req,'$..ldt_79')
# print(xn)
a=xn[0:10]
# print(xn[1:11])
datas=[]

for i in range(0,10):
    datas.append([int(a[i][0]['wl_45']),int(a[i][0]['sc_54']),int(a[i][0]['ss_d0']),int(a[i][0]['wdx_a7']),int(a[i][0]['zds_62'])])
pic = pygal.Radar()
pic._title='步枪的性能'
pic.x_labels=['威力','射程','射速','稳定性','子弹数']
for name ,data in zip(names[1:11],datas):
    print(name,data)
    pic.add(name,data)
pic.render_to_file('刺激战场.svg')

