#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/10/9 22:25
#@Author :zbwu103
#@File  ：1.py
#@功能：redis的基本使用

from redis import StrictRedis
redis =StrictRedis(host='localhost',port=6379,db=0,password='foobared')
redis.set('name','Bob')
print(redis.get('name'))
