#!/usr/bin/env python
# -*- coding:utf-8 -*-


from src.repository.user_info import UserInfoRepository
from src.repository.user_type_to_permission import UserTypeToPermissionRepository
from src.utils import commons
from config import settings

import importlib


def choice_menu():
    print('登陆成功：%s' % settings.current_user_info['username'])
    while True:
        for i, item in enumerate(settings.current_user_permission_list, 1):
            print(i, item['caption'])
        choice = input('请输入菜单：')
        choice = int(choice)
        # 获取当前选中的权限
        permission = settings.current_user_permission_list[choice - 1]

        # 获取模块路径
        module = permission['module']
        # 获取方法名
        func_name = permission['func']

        # 动态导入模块，并通过反射执行指定的方法
        m = importlib.import_module(module)
        func = getattr(m, func_name)
        func()


def find_pwd():
    pass


def register():
    # 输入用户名
    # 输入密码
    # 输入邮箱
    # 判断用户名是否存在
    obj = UserInfoRepository()
    ret = obj.exist('root')
    if ret:
        print('已经存在')
    else:
        # obj.create(...)
        pass
    # 将数据插入到userinfo表
    pass


def login():
    while True:
        username = input('请输入用户名：')
        password = input('请输入用户名：')
        pwd = commons.md5(password)
        user_repository = UserInfoRepository()
        # 当前登录的用户信息
        user_info = user_repository.fetch_by_user_pwd(username, pwd)
        if not user_info:
            print('用户名或密码错误，请重新输入.')
            continue
        type_to_per_repository = UserTypeToPermissionRepository()
        # 获取登录用户的权限信息
        permission_list = type_to_per_repository.fetch_permission_by_type_id(user_info['user_type_id'])

        # 将当前用户权限信息保存到配置中
        settings.current_user_permission_list = permission_list
        # 将当前用户信息保存到配置中
        settings.current_user_info = user_info
        return True


def execute():
    while True:
        print('欢迎登陆权限管理系统：1:登陆;2:注册;3:找回密码;\n')
        dic = {
            '1': login,
            '2': register,
            '3': find_pwd,
        }
        choice = input('请输入选项：')
        if choice not in dic.keys():
            print('选项输入错误')
            continue
        func = dic[choice]
        # 调用登录login方法，获取返回值
        result = func()
        #
        if result:
            # 登录成功后，显示所有菜单
            choice_menu()
