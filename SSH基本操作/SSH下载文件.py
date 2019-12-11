#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/3 23:55
#@Author :zbwu103
#@File  ：SSH下载文件.py
#@功能：通过SSH来下载文件


import paramiko
transport = paramiko.Transport(('192.168.43.150',22))
transport.connect(username='root',password='112423')

sftp = paramiko.SFTPClient.from_transport(transport)

localpath = '123.txt'
remotepath = '/home/wzb/zhi.txt'
sftp.get(localpath,remotepath)
transport.close()
