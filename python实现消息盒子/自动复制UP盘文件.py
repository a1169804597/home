#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/5/31 0:09
#@Author :zbwu103
#@File  ：自动复制UP盘文件.py
#@功能：自动检测U盘是否已经插入电脑，并复制U盘的文件


import os
import shutil
import time

while True:
    if os.path.exists('H:'):
       try:
            print('已检测到U盘存在')
            shutil.copytree('H:',r'C:\Users\Administrator\Desktop'+'\\'+'新建文件夹11')
            exit("复制完成")

       except Exception:
           print('复制出错')
    else:
        print('没有检测到U盘的存在')
    time.sleep(3)


