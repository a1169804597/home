#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/1 21:01
#@Author :zbwu103
#@File  ：wifi破解.py
#@功能：简单介绍pywifi的使用，分别是获取无线网卡的名称，判断网卡的连接状态，扫描附件的WiFi
import pywifi
from pywifi import const


#判断当前是否连接wifi

def gic():
    #创建一个无线的对象
    wifi=pywifi.PyWiFi()
    #获取无线网卡
    ifaces=wifi.interfaces()[0] #获取的的网卡信息是一个列表对象类型，只需要得到第一个就行了
    # print(wifi)
    #通过name()获取WiFi的名称
    print(ifaces.name())
    #打印状态码，0是没有连接，4是连接成功,1是正在扫描wifi，2是不活动的
    #3正在连接
    if ifaces.status()==const.IFACE_CONNECTED:
        print('连接成功')
    else:
        print('连接不成功')
    print(ifaces.status())
#扫描附近的WiFi
def bies():
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    #扫描WiFi
    ifaces.scan()
    #获得扫描的结果
    bessis=ifaces.scan_results()
    print(bessis)
    for name in bessis:
        #当前WiFi的名称
        print(name.ssid)
bies()


# gic()