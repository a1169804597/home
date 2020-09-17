"""djangotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('index/<data>',views.index),

    path('students/',views.students),
    path('addstudent/',views.addstudent),
    path('editorstudent/',views.editor),
    path('deletestudent/',views.deletestudent),

    path('classes/',views.classes),
    path('addclass/',views.addclass),
    path('editorclass/',views.editorclass),
    path('deleteclass/',views.deleteclass),

    path('tearchs/',views.tearchs),
    path('add_tearch/',views.add_tearch),
    path('editor_tearch/',views.editor_tearch),

    path('modal_addclass/',views.modal_addclass),
    path('modal_editorclass/',views.modal_editorclass),
    path('modal_deleteclass/',views.modal_deleteclass),

    path('modal_addstudent/',views.modal_addstudent),
    path('modal_editorstudent/',views.modal_editorstudent),

    path('modal_add_tearch/',views.modal_add_tearch),


]
