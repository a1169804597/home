#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/2 15:38
#@Author :zbwu103
#@File  ：用post请求发送B站弹幕.py
#@功能：通过输出key和主播的房间号码向发送弹幕

import requests
import time
def send_bili(key,ID):
    headers={
        "Cookie": "buvid3=7E42FFDE-1653-4B4E-86CB-5DA22523C8A640779infoc; LIVE_BUVID=AUTO9015569709199203; fts=1557158067; sid=i94ssr95; stardustvideo=1; CURRENT_FNVAL=16; rpdid=|(umR|)l|)Y~0J'ull~ul)uul; UM_distinctid=16a8ddc02b724d-08bb1982c6825d-39395704-384000-16a8ddc02b8393; finger=b3372c5f; im_notify_type_298775615=0; CURRENT_QUALITY=80; _uuid=71F322D9-39F3-41BE-E54A-DEE43F8EA95440070infoc; bp_t_offset_298775615=259796648981299209; _dfcaptcha=129df7de545d489e4f4f952dd268515a; GIFT_BLOCK_COOKIE=GIFT_BLOCK_COOKIE; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1559461128,1559461215,1559461329; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1559461329; DedeUserID=298775615; DedeUserID__ckMd5=77e1f7592bbce6d3; SESSDATA=b846f8ff%2C1562053771%2Cd4d2e261; bili_jct=4dfe5eb34a9a8fe903408763ea6aac84",
        "Host": "live.bilibili.com",
        "Referer": "https://www.bilibili.com/",
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'73.0.3683.103 Safari/537.36",
    }
    data={
        "color": "16777215",
        "fontsize": "25",
        "mode": "1",
        "msg": key,
        "rnd": "1559462795",
        "roomid": ID,#主播房间的ID
        "bubble": "0",
        "csrf_token": "4dfe5eb34a9a8fe903408763ea6aac84",
        "csrf": "4dfe5eb34a9a8fe903408763ea6aac84"
    }
    url="https://api.live.bilibili.com/msg/send"

    response=requests.post(url,headers=headers,data=data)
    if response.status_code==200:
        print("发送成功")
if __name__=='__main__':

    while True:
        key=input("请输入要发送的弹幕")
        ID=input("请输入主播的房间编号: ")
        send_bili(key,ID)
        time.sleep(20)