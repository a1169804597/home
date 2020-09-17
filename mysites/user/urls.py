#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2020/3/24 0:57
#@Author :zbwu103
#@File  ：urls.py
#@功能：

from django.urls import  path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login_for_medal/', views.login_for_medal, name='login_for_medal'),
    path('register/', views.register, name='register'),
    path('user_info',views.user_info,name='user_info'),
    path('logout/',views.login_out,name='logout'),
    path('change_nickname/',views.change_nickname,name='change_nickname'),
    path('bind_email/',views.bind_email,name='bind_email'),
    path('send_verification_code/',views.send_verification_code,name='send_verification_code'),
    path('change_password/',views.change_password,name='change_password'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
]