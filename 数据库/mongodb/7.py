#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/10/9 21:35
#@Author :zbwu103
#@File  ：4.py
#@功能：计数

import pymongo
client=pymongo.MongoClient(host='localhost',port=27017)
#指点数据库的名称是test
db=client.test
#指定数据库的集合名称为students
collection=db.students
results = collection.find().count()
print(results)
