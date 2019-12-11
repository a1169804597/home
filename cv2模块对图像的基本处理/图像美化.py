#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/15 17:01
#@Author :zbwu103
#@File  ：图像美化.py
#@功能：传入一张图片，对图片进行美化。

import cv2

image=cv2.imread('test.jpg')

#实现美颜的效果
value=20

new_image=cv2.bilateralFilter(image,value,value*2,value/2)
cv2.imwrite('new_test.jpg',new_image)

