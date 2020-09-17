#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/14 21:14
#@Author :zbwu103
#@File  ：王者刷金币脚本.py
#@功能：控制手机王者荣耀刷金币


import os,time

i=1
while True:
    dir="D:\\小工具\\adb\\platform-tools"
    #点击闯关按键
    os.system("%s\\adb shell input tap 1434 880 "%dir)
    #等待加载游戏
    time.sleep(10)
    #等待游戏运行
    time.sleep(60)
    #点击继续按键
    os.system("%s\\adb shell input tap 943 956 "%dir)
    time.sleep(4)
    #点击再次挑战
    os.system("%s\\adb shell input tap 1620 1005 "%dir)
    time.sleep(7)
    i+=1
    print("游戏运行第%s次"%i,flush=True)
