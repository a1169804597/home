#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/15 16:47
#@Author :zbwu103
#@File  ：色彩变换.py
#@功能：
import cv2


im = cv2.imread("source/bug.png")
#cv2.COLOR_X2Y
# 其中X,Y = RGB, BGR, GRAY, HSV, YCrCb, XYZ, Lab, Luv, HLS
new_img = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
cv2.imwrite("source/bug-gray.png", new_img)
