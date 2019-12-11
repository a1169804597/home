#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/16 8:38
#@Author :zbwu103
#@File  ：获取微信头像墙.py
#@功能：获取微信好友的头像，并且把头像做成一张头像墙。

import itchat,os,math
import PIL.Image as Image

#登入微信
itchat.auto_login(hotReload=True)
#获取好友的列表信息
friends=itchat.get_friends()
if not os.path.exists("img"):
    os.mkdir("img")
num=0
# for friend in friends:
#     try:
#         #获取头像图片
#         img=itchat.get_head_img(userName=friend['UserName'])
#         #保存图片
#         with open('img'+'\\'+str(num)+'.png','wb') as f:
#             f.write(img)
#         if  Image.open("img" + '\\' + str(num) + '.png'):
#             num+=1
#     except OSError:
#         print("第%s张图片错误，无法打开"%num)
#确定微信有多少张图片
images=os.listdir("img")
# print(len(images))
each_size=int(math.sqrt((640*640)/len(images)))
print(each_size)
#每行可以容纳多少头像
lines=int(640/each_size)
#创建一个空白图片对象
image=Image.new('RGBA',(640,640))

x=0
y=0
#一张一张的去粘贴
for i in range(0,len(images)):
    #打开头像
    img=Image.open("img"+'\\'+str(i)+'.png')
    #缩放我们头像的尺寸,Image.ANTIALIAS是设置图片的清晰度
    img.resize((each_size,each_size),Image.ANTIALIAS)
    #粘贴img这张图片到我们的空白图片上去
    image.paste(img,(x*each_size,y*each_size))
    x+=1
    if x==lines-1:
        #一行粘贴满了，粘贴下一行
        x=0
        #进入下一行
        y+=1
image.save('img'+'\\'+'all.png')