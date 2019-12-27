from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    #/http://localhost/blog
    path('',views.blog_list,name='blog_list'),
    path('<int:blog_pk>',views.blog_detail,name='blog_detail'),
    path('type<blog_type_pk>',views.blogs_with_type,name="blogs_with_type"),
    path('data/<int:year>/<int:month>',views.blogs_with_date,name='blogs_with_date'),

]