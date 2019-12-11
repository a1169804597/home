#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/3 23:18
#@Author :zbwu103
#@File  ：连接SSH.py
#@功能：通过SSH连接和CRT类似

import paramiko

transport = paramiko.Transport(('192.168.43.150',22))
transport.connect(username='root',password='112423')

ssh = paramiko.SSHClient()
ssh._transport = transport
comm = input(":>>")
while comm != 'q':
    stdin,stdout,stderr = ssh.exec_command(comm)
    err = stderr.read()
    if err:
        re_msg = err
    else:
        re_msg = stdout.read()

    print(re_msg.decode('gbk'))
    comm = input(":>>")