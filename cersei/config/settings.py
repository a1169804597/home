#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 当前登录用户的权限列表
# ...
current_user_permission_list = []

# 当前登录用户的基本信息：
# {'nid':1,'username': 'root', 'role_id': 1}
current_user_info = {}

PY_MYSQL_CONN_DICT = {
    "host": '127.0.0.1',
    "port": 3306,
    "user": 'root',
    "passwd": '666',
    "db": 'authdb',
    "charset": 'utf8'
}
# import pymysql
# # pymysql.connect(**kwargs)
# pymysql.connect(host='localhost',port=3306)
# pymysql.connect(**{'host':'locahost','port': 3306})