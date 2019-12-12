#！/E:\python\env\python37\Scripts
# -*- coding:utf-8 -*-
#@Time  :2019/6/2 17:51
#@Author :zbwu103
#@File  ：1.py
#@功能：模拟QQ邮件发送邮件
import requests


class QQSend:
    def __init__(self,url,headers,data):
        self.url=url
        self.headers=headers
        self.data=data
    def send(self):
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data)
            if response.status_code==200:
                print('邮件发送成功')
            else:
                print("邮件发送失败")
        except Exception:
            print("发生错误")
def main(data,targe):
    url = "https://mail.qq.com/cgi-bin/compose_send?sid=p4WVX_JuqJJhFEwQ"
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "eas_sid=D195Y5S836j2d6O7T8s5x8G969; LW_sid=c1W555O8s6i2J6d7D8E5S9R064; LW_uid=T1h5V5H8t6k2u6v788G5s9a0B6; pgv_pvi=8236238848; pgv_pvid=3274416156; bRankChanged=TRUE; rankv=2019051711; pgv_si=s9866493952; ptisp=; ptui_loginuin=1480244514@qq.com; uin=o1480244514; skey=@d0f2pkRqP; RK=3gpMlV9oap; ptcz=6d8636f433c48632395aa340e0917b5fe8d44638811e4fbff7897098e559b816; p_uin=o1480244514; pt4_token=LxSsFssrkHGDbDBnziIZ7XI7xrgoVqPbb7KKBXs1S7s_; p_skey=1rvnZH4TxmyjATMFHWuINtnn5*YGw7ual2u9Ah1efgo_; wimrefreshrun=0&; qm_logintype=qq; qm_flag=0; qqmail_alias=1480244514@qq.com; sid=1480244514&3fd90ab327b22dea2f53a5cea3da505d,qMXJ2blpINFR4bXlqQVRNRkhXdUlOdG5uNSpZR3c3dWFsMnU5QWgxZWZnb18.; qm_username=1480244514; qm_domain=https://mail.qq.com; qm_ptsk=1480244514&@d0f2pkRqP; foxacc=1480244514&0; ssl_edition=sail.qq.com; edition=mail.qq.com; qm_loginfrom=1480244514&wpt; username=1480244514&1480244514; CCSHOW=000001; new_mail_num=1480244514&41; webp=1; qm_sid=3fd90ab327b22dea2f53a5cea3da505d,qMXJ2blpINFR4bXlqQVRNRkhXdUlOdG5uNSpZR3c3dWFsMnU5QWgxZWZnb18.",
        "origin": "https://mail.qq.com",
        "referer": "https://mail.qq.com/zh_CN/htmledition/ajax_proxy.html?mail.qq.com&v=140521",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
    }
    data = {
        "6ba95767529a3f34e93ef07d5ea07fba": "3fd90ab327b22dea2f53a5cea3da505d",
        "sid": "p4WVX_JuqJJhFEwQ",
        "from_s": "cnew",
        "to": targe,
        "subject": data,
        "content__html": "<div>asdasdasdasd</div>",
        "sendmailname": "1480244514@qq.com",
        "savesendbox": "1",
        "actiontype": "send",
        "sendname": "机器人",
        "acctid": "0",
        "separatedcopy": "false",
        "s": "comm",
        "hitaddrbook": "0",
        "selfdefinestation": "-1",
        "domaincheck": "0",
        "cgitm": "1559465251900",
        "clitm": "1559465252044",
        "comtm": "1559465284585",
        "logattcnt": "0",
        "logattsize": "0",
        "cginame": "compose_send",
        "ef": "js",
        "t": "compose_send.json",
        "resp_charset": "UTF8"
    }
    return url,headers,data
if __name__=="__main__":
    data=input("输入要发送的邮件内容：")
    targe=input("请输入要发送的目标邮件格式是xxxxxx<xxxxx@.qq.com>:")
    url,headers,data=main(data,targe)
    qqsend=QQSend(url,headers,data)
    qqsend.send()