#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/5/26 18:32
#@Author :zbwu103
#@File  ：1.py
#@功能：用Python实现VIP电影免费观看

import requests
import re
import tkinter as tk
import webbrowser
url = 'http://www.qmaile.com/'
req = requests.get(url)
# req.encoding='utf-8'
req.encoding = req.apparent_encoding

reg=re.compile('<option value="(.*?)" selected="">',re.S)
res=re.findall(reg,req.text)

one = res[0]
two = res[1]
three = res[2]
four = res[3]
five = res[4]
print(one)
root = tk.Tk()
root.geometry('500x250')
root.title('vip电影播放')
l1 = tk.Label(root,text='播放接口',font=('微软雅黑',12))
l1.grid()
#设置tk的变量
var = tk.StringVar()

r1=tk.Radiobutton(root,text='播放接口1',variable=var,value=one)
r1.grid(row=0,column=1)
r2=tk.Radiobutton(root,text='播放接口2',variable=var,value=two)
r2.grid(row=1,column=1)
r3=tk.Radiobutton(root,text='播放接口3',variable=var,value=three)
r3.grid(row=2,column=1)
r4=tk.Radiobutton(root,text='播放接口4',variable=var,value=four)
r4.grid(row=3,column=1)
r5=tk.Radiobutton(root,text='播放接口5',variable=var,value=five)
r5.grid(row=4,column=1)
l2 = tk.Label(root,text='播放链接',font=('微软雅黑',12))
l2.grid(row=5,column=0)

e1 = tk.Entry(root,text='',width=50)
e1.grid(row=5,column=1)
#选择一个选择按钮，你就会得到一个解析接口，当你打开一个网站（解析接口和输入框的内容）
#使用这个bf函数来写这个按钮和解析接口
def bf():
    webbrowser.open(var.get()+e1.get())

b1 = tk.Button(root,text='播放',font=12,width=8,command=bf)
b1.grid(row=6,column=1)
#清除输入框中的东西
def qc():
    e1.delete(0,'end')
b2 =tk.Button(root,text='清除',font=12,width=8,command=qc)
b2.grid(row=7,column=1)
root.mainloop()

