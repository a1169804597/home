#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/12/16 23:33
#@Author :zbwu103
#@File  ：urls.py
#@功能：


from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    #/http://localhost/blog
    path('<int:blog_pk>',views.blog_detail,name='blog_detail'),
    path('/type<blog_type_pk>',views.blogs_with_type,name="blogs_with_type")
]