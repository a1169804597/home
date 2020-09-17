#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/11 22:09
#@Author :zbwu103
#@File  ：dingding.py
#@功能：

import os,time
import smtplib
from email.mime.text import MIMEText

#adb存放的路径
directory="D:\\小工具\\adb\\platform-tools"
#上班打卡的时间
go_hour=8
#下班打卡的时间
back_hour=18
#发送方邮箱
msg_from='1480244514@qq.com'
#填入发送方邮箱的授权码
passwd='widqivdddmmofhgb'
#收件人邮箱
msg_to='1169804597@qq.com'
#打卡结果截图保存地址
screen_dir="C:\\Users\\Administrator\\Desktop\\screen_dir"
#点亮屏幕
adbpower="%s\\adb shell input keyevent 26 "%directory
#上滑解锁滑动
adbclear="%s\\adb shell input swipe 300 1000 300 200 500"%directory
#先关闭钉钉之后再打开钉钉
adbkill_dingding="%s\\adb shell am force-stop com.alibaba.android.rimet"%directory
adbopen_dingding="%s\\adb shell monkey -p com.alibaba.android.rimet -c android.intent.category.LAUNCHER 1"%directory
#返回
# adbback_work="%s\\adb shell input keyevent 3 "%directory
#点击工作
adbselect_work="%s\\adb shell input tap 548 1823  "%directory
# 点击考勤打卡
adbselect_playcard="%s\\adb shell input tap 136 1066  "%directory
#设备截图保存到sdcard中
adbscrttncap="%s\\adb shell screencap -p /sdcard/screen.png  "%directory
#把截图传送到电脑
adbpull="%s\\adb pull sdcard/screen.png  C:\\Users\\Administrator\\Desktop\\screen_dir"%directory
def go_work():
    os.system(adbpower)
    time.sleep(1)
    os.system(adbclear)
    time.sleep(3)
    os.system(adbkill_dingding)
    time.sleep(1)
    os.system(adbopen_dingding)
    time.sleep(3)
    # 点击工作
    os.system(adbselect_work)
    time.sleep(3)
    # 点击考勤打卡
    os.system(adbselect_playcard)
    os.system(adbscrttncap)
    time.sleep(1)
    os.system(adbpull)
def back_work():
    os.system(adbpower)
    time.sleep(1)
    os.system(adbclear)
    time.sleep(3)
    os.system(adbkill_dingding)
    time.sleep(1)
    os.system(adbopen_dingding)
    time.sleep(3)
    # 点击工作
    os.system(adbselect_work)
    time.sleep(3)
    # 点击考勤打卡
    os.system(adbselect_playcard)
    #下班点击打卡还没有弄

    os.system(adbscrttncap)
    time.sleep(1)
    os.system(adbpull)
def sendmail():
    # 主题
    subject = "钉钉打卡邮件"
    # 正文
    content = "请注意查看钉钉打卡是否成功"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    try:
        # 邮件服务器及端口号
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录SMTP服务器
        s.login(msg_from, passwd)
        # 发邮件 as_string()把MIMEText对象变成str
        s.sendmail(msg_from, msg_to, msg.as_string())
        print("发送成功")
    except s.SMTPException:
        print("发送失败")
    finally:
        s.quit()
go_work()