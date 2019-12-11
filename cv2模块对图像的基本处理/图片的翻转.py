#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/15 16:41
#@Author :zbwu103
#@File  ：图片的翻转.py
#@功能：

import cv2

im = cv2.imread("source/bug.png")
#沿着X轴垂直翻转flipCode为0，沿着Y轴水平翻转flipCode为1，水平和垂直都翻转的话，
# 沿着中心点翻转的话是flipCode为-1
new_img = cv2.flip(im, flipCode=0)
cv2.imwrite("source/bug-flip-0.png", new_img)