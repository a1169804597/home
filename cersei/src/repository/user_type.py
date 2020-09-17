#!/usr/bin/env python
# -*- coding:utf-8 -*-
from src.utils.db_connection import DbConnection


class UserTypeRepository:
    def __init__(self):
        self.db_conn = DbConnection()

    def add(self, caption):
        """
        根据用户名密码获取账户信息
        :param username:
        :param password:
        :return:
        """
        cursor = self.db_conn.connect()
        sql = """
          insert into user_type(caption) values(%s)
        """
        cursor.execute(sql, [caption,])
        self.db_conn.close()

