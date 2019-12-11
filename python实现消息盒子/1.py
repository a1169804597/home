#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/5/26 15:03
#@Author :zbwu103
#@File  ：1.py
#@功能：用tkinter库制作一个消息盒子

import tkinter as tk
from PIL import ImageTk
from tkinter import messagebox


# 喜欢子窗口，按键窗口
def love():
    love_root=tk.Toplevel(root)
    love_root.title('嘻嘻！')
    l4=tk.Label(love_root,text='好巧啊，我也是',font=('微软雅黑',24))
    l4.pack()
                                                #点击子款的确定，摧毁主框的程序
    b3=tk.Button(love_root,text='确定',font=('微软雅黑',24),command=root.destroy)
    b3.pack()

# 不喜欢子窗口，按键窗口
def no_love():
    no_love_root=tk.Toplevel(root)
    no_love_root.title('在考虑下呗')
    l4=tk.Label(no_love_root,text='...= =...',font=('微软雅黑',24))
    l4.pack()                                                 #no_love_root,destroy 点击确定关闭子框
    b3=tk.Button(no_love_root,text='确定',font=('微软雅黑',24),command=no_love_root.destroy)

    #点击红叉时不关闭程序，并且再打开一个相同的子框
                        #点击红叉         调用本身子款
    no_love_root.protocol("WM_DELETE_WINDOW",no_love)
    b3.pack()

#消息盒子，关闭程序的时候阻止关闭
def close_window():
    messagebox.showerror(title='提示',message='再想想')

root = tk.Tk()
root.title('你喜欢我嘛')
root.geometry('510x460+250+100')  #弹窗的大小
l1 = tk.Label(root,text='hey,小姐姐',font=('微软雅黑',14),fg='red')
l1.grid(sticky=tk.W) #摆放位置，用网格式的布局
l2 = tk.Label(root,text='喜欢我嘛',font=('微软雅黑',30))
l2.grid(row=1,column=1,sticky=tk.E) #摆放位置，用网格式的布局
#图片显示
bm=ImageTk.PhotoImage(file='./test.jpg')
l3=tk.Label(root,image=bm)
l3.grid(row=2,columnspan=2)
#点击红叉阻止关闭程序
root.protocol("")
#下面的按键显示
b1 =tk.Button(root,text='喜欢',width=15,height=2,command=love)
b1.grid(row=3,column=0,sticky=tk.W)

b2 =tk.Button(root,text='不喜欢',width=5,height=2,command=no_love)
b2.grid(row=3,column=1,sticky=tk.E)
#点击红叉之后，在重新打开一个主框
root.protocol("WM_DELETE_WINDOW",close_window)
root.mainloop()