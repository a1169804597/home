#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/15 16:50
#@Author :zbwu103
#@File  ：给图片加文字.py
#@功能：这个添加文字的话，只能加入字符不能加入中文字符
import cv2


img = cv2.imread("source/bug.png", cv2.IMREAD_COLOR)

# 图片对象、文本、像素、字体、字体大小、颜色、字体粗细
new_img = cv2.putText(
    img=img,
    text="oooooooooo",
    org=(60, 50),
    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    fontScale=1,
    color=(255, 0, 0),
    thickness=2
)
cv2.imwrite("source/bug-text.png", new_img)

