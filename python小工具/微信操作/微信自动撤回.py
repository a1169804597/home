#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/15 22:10
#@Author :zbwu103
#@File  ：微信自动撤回.py
#@功能：开启后，收到好友发送的消息之后，如果好友把消息撤回之后，程序将把撤回的消息自动保存到文件中（文字，语音，图片）


import itchat,os,re
import time

#保存撤回消息的路径
temp="D:\\python\\项目\\venv\\python小工具\\微信操作\\temp"
if not os.path.exists(temp):
    os.mkdir(temp)
itchat.auto_login(hotReload=True)
#itchat.content.TEXT是文本消息，itchat.content.PICTURE是图片消息，其他消息好像暂时无法实现
@itchat.msg_register([itchat.content.TEXT,itchat.content.RECORDING,itchat.content.PICTURE ])#装饰器，给我们下面的函数添加新功能,好友发的消息储存在msg中
def resever_info(msg):
    global info_T,info_type,name_R
    info_T=msg['Text']
    info_type=msg['Type']
    name_R=msg['FileName']
    print(msg)
@itchat.msg_register(itchat.content.NOTE)#NOTE是系统消息，收到的是系统给我们发的一条消息
def chehui_info(chehui_msg):
    global info_T,info_type,name_R

    if "撤回了一条消息" in chehui_msg["Text"]:
        if info_type=='Recording':
            info_T(temp+'\\'+name_R)
        elif info_type=='Text':
            # 获取当前的时间
            # 用正则表达式获取撤回人微信名称
            reg = re.compile("\"(.*?)\"", re.S)
            res = re.search(reg, chehui_msg['Text'])
            chehui_name = res.group(1)
            nowtime=time.strftime("%m-%d-%H:%M", time.localtime(time.time()))
            with open(temp+'\\'+chehui_name+'.txt',"ab") as f:
                f.write((nowtime+" :"+info_T+'\n').encode('utf-8'))
        elif  info_type=='Picture':
            info_T(temp + '\\' + name_R)
itchat.run()