#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/10/9 21:02
#@Author :zbwu103
#@File  ：1.py
#@功能：mongodb的存储

import pymongo
#连接mongodb
client=pymongo.MongoClient(host='localhost',port=27017)
#指点数据库的名称是test
db=client.test
#指定数据库的集合名称为students
collection=db.students
student={
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
#使用.insert()方法来插入数据
result=collection.insert_one(student)
print(result)
print(result.inserted_id)