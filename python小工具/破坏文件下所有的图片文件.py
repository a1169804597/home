     #！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/5/31 0:31
#@Author :zbwu103
#@File  ：破坏文件下所有的图片文件.py
#@功能：慎用！！！！！！！破坏文件下所有的图片

import os
file_path=r'C:\Users\Administrator\Desktop\新建文件夹 (2)'
def pk_img(file_path):
    for i in os.listdir(file_path):
        path=os.path.join(file_path,i)
        if os.path.isdir(path):
            print("%s是文件夹，准本进入文件夹"%i)
            pk_img(path)
        elif os.path.isfile(path):
            if i.endswith('.png') or i.endswith('.jpg'):
                with open(path, 'w+b') as f:
                #以写的的方式来读取图片的信息，来破环图片
                    conten=f.read()
                print('破坏成功')




if __name__=='__main__':
    pk_img(file_path)