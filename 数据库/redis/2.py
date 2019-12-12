#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/10/9 22:25
#@Author :zbwu103
#@File  ：1.py
#@功能：redis的基本使用使用URL来获取

from redis import StrictRedis ,ConnectionPool
url = 'redis://:foobared@localhost:6379/0'
pool = ConnectionPool.ramurl(url)
redis = StrictRedis(connection_pool=pool)


