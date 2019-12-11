#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/15 16:30
#@Author :zbwu103
#@File  ：简单的读写操作.py
#@功能：

import cv2

#读入图像
img=cv2.imread("source/bug.png")

#显示图像
cv2.imshow("bug",img)
cv2.waitKey(0)
cv2.destroyWindow('bug')

#复制图片
new_img=img.copy()
#保存图片,当前目录下
cv2.imwrite("bug-new.png",new_img)

