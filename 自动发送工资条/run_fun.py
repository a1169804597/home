import os
from openpyxl import load_workbook
import smtplib
from email.mime.text import MIMEText  #邮件正文
from email.header import Header #邮件头

account = "1480244514@qq.com"
SEND_EMAIL = "1480244514@qq.com"
# password = "idwkkclcarvijgca"
password = "pfgzkdpfglzybacj"
smtp_obj = smtplib.SMTP_SSL("smtp.qq.com", 465)
smtp_obj.login(account, password)


def send_email(send_email=SEND_EMAIL, data_info=None):
    mail_body = f'''
                <h5> hello, {data_info["name"]}</h5>
                <p>
                    您的工资凭条为附件的内容，密码为你的身份证的后四位，请注意查收！
                </p>
                <table border="1px solid black">
                    <tr>
                        <th>姓名</th>
                        <th>部门</th>
                        <th>基本工资</th>
                        <th>绩效工资</th>
                        <th>提成</th>
                        <th>电脑补贴</th>
                        <th>社保</th>
                        <th>请假</th>
                        <th>公积金</th>
                        <th>专业扣除</th>
                        <th>累计应缴所h税</th>
                        <th>累计应缴税h</th>
                        <th>实发工资</th>
                    </tr>
                    <tr>
                        <td>{data_info["name"]}</td>
                        <td>{data_info["department"]}</td>
                        <td>{data_info["base_wages"]}</td>
                        <td>{data_info["merits_wages"]}</td>
                        <td>{data_info["commission"]}</td>
                        <td>{data_info["computer_subsidy"]}</td>
                        <td>{data_info["social_security"]}</td>
                        <td>{data_info["leave"]}</td>
                        <td>{data_info["accumulation"]}</td>
                        <td>{data_info["special_deduction"]}</td>
                        <td>{data_info["payable"]}</td>
                        <td>{data_info["cumulative_payable"]}</td>
                        <td>{data_info["actual_wages"]}</td>
                    </tr>
                    
                </table>
               '''
    msg = MIMEText(mail_body, "html", "utf-8")
    msg["From"] = Header("大唐集团财务部", "utf-8") #发送者
    msg["To"] = Header("大唐员工", "utf-8") #接受者
    msg["Subject"] = Header("工资凭条，请注意保管") #主题
    smtp_obj.sendmail(send_email, data_info["email"], msg.as_string())
    print("工资发工资到{}成功".format(data_info["name"]))


def read_excel():
    wb = load_workbook("大唐集团工资条.xlsx",data_only=True)
    sheet = wb.active
    i = 1

    for row in sheet:
        data_info = {}
        if i == 1 and row[1].value == "邮箱" and row[2].value == "姓名":
            pass
            i += 1
        elif row[2].value == None:
            break
        else:
            data_info["email"] = row[1].value
            data_info["name"] = row[2].value
            data_info["department"] = row[3].value
            data_info["base_wages"] = row[4].value
            data_info["merits_wages"] = row[5].value
            data_info["commission"] = row[6].value
            data_info["computer_subsidy"] = row[7].value
            data_info["social_security"] = row[8].value
            data_info["leave"] = row[9].value
            data_info["accumulation"] = row[10].value
            data_info["special_deduction"] = row[11].value
            data_info["payable"] = row[12].value
            data_info["cumulative_payable"] = row[13].value
            data_info["actual_wages"] = row[14].value
            for key, value in data_info.items():
                if value == None:
                    data_info[key] = ""
            # send_email(data_info=data_info)
        print(row[2].value)



if __name__ == '__main__':
    read_excel()
