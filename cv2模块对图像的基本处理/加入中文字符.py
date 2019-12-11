#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/15 16:53
#@Author :zbwu103
#@File  ：加入中文字符.py
#@功能：

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 1、将cv2转为PIL
img = cv2.imread("source/bug.png")
# cv2和PIL中颜色的hex码的储存顺序不同
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
pil_img = Image.fromarray(img)

# 2、PIL图片上打印中文
draw = ImageDraw.Draw(pil_img)
font = ImageFont.truetype(font="华文黑体.ttf", size=20, encoding="utf-8")
draw.text(xy=(50, 20), text="爱我中华", fill=(0, 0, 255), font=font)

# 3、PIL图片转cv2
new_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
cv2.imwrite("source/bug-text.png", new_img)

