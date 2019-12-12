from flask import Flask
from flask import render_template
from flask import request
import csv

with open("签到表单.csv",'a',newline='') as f:
    csvwrite = csv.writer(f, dialect='excel')
    csvwrite.writerow(["姓名", "性别", "手机", "部门"])

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('html1.html')
@app.route('/s')
def log():
    return render_template('html2.html')
@app.route('/m')
def cg():
    name=request.args.get("name")
    sex=request.args.get("sex")
    iphone = request.args.get("iphone")
    deparment= request.args.get("deparment")
    print(name,sex,iphone,deparment)

    with open("签到表单.csv",'a',newline='') as f:
        csvwrite = csv.writer(f,dialect='excel')
        csvwrite.writerow([name,sex,iphone,deparment])
    return render_template('html3.html')
app.run()