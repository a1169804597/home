#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/1 22:03
#@Author :zbwu103
#@File  ：pwd.py.py
#@功能：输入数字样式，生成N位包含这些数字所有样式的密码本

import itertools as its  #迭代器



words='1234567890'

r=its.product(words,repeat=4)
with open("pass.txt",'a') as f:
    #生成标准格式的密码本
    for i in r:
        #打印的是一个元组
        # print(i)
        f.write("".join(i))
        f.write("".join('\n'))



