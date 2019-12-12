#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/10/9 21:02
#@Author :zbwu103
#@File  ：1.py
#@功能：在mongodb中插入多条数据

import pymongo
#连接mongodb
client=pymongo.MongoClient(host='localhost',port=27017)
#指点数据库的名称是test
db=client.test
#指定数据库的集合名称为students
collection=db.students
student1={
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}
student2={
    'id':'20170202',
    'name':'Mike',
    'age':21,
    'gender':'male',
}
#使用.insert()方法来插入数据,使用列表的方式同时插入两条数据
result=collection.insert([student1,student2])
print(result)