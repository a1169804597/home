#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/11 22:09
#@Author :zbwu103
#@File  ：dingding.py
#@功能：钉钉打卡，通过adb连接手机，上午7点四十进行签到，下午5点半签退，晚上八点半更新打卡

import os,time
import smtplib
from email.mime.text import MIMEText
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#公司电脑adb存放的路径
directory="D:\\adb\platform-tools_r28.0.3-windows\\platform-tools"
# #家里电脑adb存放的路径
# directory="D:\\小工具\\adb\\platform-tools"
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
# #打卡结果截图保存家里地址
# screen_dir="C:\\Users\\Administrator\\Desktop\\screen_dir"
#打卡结果截图保存公司电脑地址
screen_dir="C:\\Users\\admin\\Desktop\\screen_dir"
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
adbselect_work="%s\\adb shell input tap 537 1833  "%directory
# 点击考勤打卡
adbselect_playcard="%s\\adb shell input tap 145 1105  "%directory
#设备截图保存到sdcard中
adbscrttncap="%s\\adb shell screencap -p /sdcard/screen.png  "%directory
#把截图传送到公司电脑电脑
adbpull="%s\\adb pull sdcard/screen.png  C:\\Users\\admin\\Desktop\\screen_dir"%directory
# #家里电脑
# adbpull="%s\\adb pull sdcard/screen.png  C:\\Users\\Administrator\\Desktop\\screen_dir"%directory
#下班点击打卡
adbselect_daka="%s\\adb shell input tap 529 1109  "%directory
#更新打卡
adbgengxin_daka="%s\\adb shell input tap 176 1135  "%directory
adbqueding_daka="%s\\adb shell input tap 835 1074  "%directory
def go_work():
    os.system(adbpower)
    time.sleep(2)
    os.system(adbclear)
    time.sleep(2)
    os.system(adbkill_dingding)
    time.sleep(1)
    print("正在打开钉钉")
    os.system(adbopen_dingding)
    # 点击工作
    time.sleep(17)
    os.system(adbselect_work)
    # 点击考勤打卡
    time.sleep(17)
    print("进入考勤打卡界面")
    os.system(adbselect_playcard)
    #截图发送到电脑上的screen_dir文件夹
    time.sleep(17)
    os.system(adbscrttncap)
    os.system(adbpull)
    print("打卡截图已保存到电脑screen_dir文件夹 ")
    # 打卡完毕之后关闭屏幕
    os.system(adbpower)
def back_work():
    os.system(adbpower)
    time.sleep(2)
    os.system(adbclear)
    time.sleep(2)
    os.system(adbkill_dingding)
    time.sleep(1)
    print("正在打开钉钉")
    os.system(adbopen_dingding)
    # 点击工作
    time.sleep(17)
    os.system(adbselect_work)
    # 点击考勤打卡
    time.sleep(17)
    print("进入考勤打卡界面")
    os.system(adbselect_playcard)
    # 下班点击打卡
    time.sleep(17)
    os.system(adbselect_daka)
    # 截图发送到电脑上的screen_dir文件夹
    time.sleep(17)
    os.system(adbscrttncap)
    os.system(adbpull)
    print("打卡截图已保存到电脑screen_dir文件夹 ")
    # 打卡完毕之后关闭屏幕
    os.system(adbpower)
def gengx():
    os.system(adbpower)
    time.sleep(2)
    os.system(adbclear)
    time.sleep(2)
    os.system(adbkill_dingding)
    time.sleep(1)
    print("正在打开钉钉")
    os.system(adbopen_dingding)
    # 点击工作
    time.sleep(17)
    os.system(adbselect_work)
    # 点击考勤打卡
    time.sleep(17)
    print("进入考勤打卡界面")
    os.system(adbselect_playcard)
    #更新打卡记录
    time.sleep(17)
    os.system(adbgengxin_daka)
    time.sleep(5)
    os.system(adbqueding_daka)
    # 截图发送到电脑上的screen_dir文件夹
    time.sleep(17)
    os.system(adbscrttncap)
    os.system(adbpull)
    print("打卡截图已保存到电脑screen_dir文件夹 ")
    #打卡完毕之后关闭屏幕
    os.system(adbpower)
def sendmail():
    # 主题
    msg_to = '1169804597@qq.com'
    subject = "钉钉打卡邮件"
    # 正文
    msg = MIMEMultipart('related')
    content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')
    msg.attach(content)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to
    #家里地址
    # file = open("C:\\Users\Administrator\\Desktop\screen_dir\\screen.png", "rb")
    # 公司地址
    file = open("C:\\Users\\admin\\Desktop\\screen_dir\\screen.png", "rb")
    img_data = file.read()
    file.close()
    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    msg.attach(img)
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
def main():
    nowtime = datetime.datetime.now()
    try:
        if int(nowtime.hour)<8:
            print("上班打卡")
            go_work()
        elif int(nowtime.hour)>17 and int(nowtime.hour)< 18 :
            print("下班打卡")
            back_work()
        elif int(nowtime.hour)>20 :
            gengx()
    except Exception:
        print("打卡中中途出错，重新进行3次打卡，如果还是出错则停止并发送邮件通知")
        i=3
        while True:
            time.sleep(120)
            if i<1 :
                break
            else:
                if int(nowtime.hour) < 8:
                    print("%s次重试上班打卡"%(4-i))
                    go_work()
                if int(nowtime.hour) > 14:
                    print("%s次重试下班打卡" % (4 - i))
                    print("下班打卡")
                    back_work()
            i-=1
    # 打卡成功发送邮件
    sendmail()
if __name__=="__main__":
    main()