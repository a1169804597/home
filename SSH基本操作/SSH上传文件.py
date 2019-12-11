#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/3 23:20
#@Author :zbwu103
#@File  ：SSH上传文件.py
#@功能：通过SSH上传文件


import paramiko
transport = paramiko.Transport(('192.168.43.150',22))
transport.connect(username='root',password='112423')

helei = paramiko.SFTPClient.from_transport(transport)
# 本地文件的地址
localpath = r'D:\python\项目\venv\SSH基本操作\pass.txt'
# 目标文件的地址linux中是以/来分割的
remotepath = '/home/wzb/zhi.txt'
helei.put(localpath,remotepath)
transport.close()
