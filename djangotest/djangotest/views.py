from django.shortcuts import render ,redirect
from django.http import HttpResponse,JsonResponse
from utils.sqlheper import SqlHeper

def index(request,data):
    print(data)
    return render(request,'home.html')

def home(request):

    context = {}
    return render(request, 'home.html', context)


def students(request):
    sqlhepr = SqlHeper()
    result = sqlhepr.select_all_data("select students.id, students.name,students.class_id, classes.title from students left JOIN classes on students.class_id = classes.id",[])
    class_list = sqlhepr.select_all_data("select id ,title from classes ",[])
    sqlhepr.close_data()
    context = {}
    context['students'] = result
    context['class_list'] = class_list
    return render(request,'students.html',context)

def addstudent(request):
    sqlhepr = SqlHeper()
    if request.method == 'POST':
        student_name = request.POST.get('addstudent')
        class_id = request.POST.get('class_name')
        sqlhepr.insert_data("insert into students (name,class_id) value(%s,%s)",[student_name,class_id])
        sqlhepr.commit_data()
        sqlhepr.close_data()
        return redirect('/students/')
    else:
        class_list = sqlhepr.select_all_data("select * from classes",[])
        context = {}
        context['class_list'] = class_list
        sqlhepr.close_data()
        return render(request,'addstudent.html',context)

def editor(request):
    nid = request.GET.get('nid')
    sqlhepr = SqlHeper()
    if request.method == "POST":
        name = request.POST.get('editor')
        class_id = request.POST.get('class_name')
        sqlhepr.updata_data("update students set name=%s,class_id=%s where id=%s", [name,class_id,nid])
        sqlhepr.commit_data()
        sqlhepr.close_data()
        return redirect('/students/')
    else:
        result = sqlhepr.select_one_data("select id,name ,class_id from students where id=%s", [nid, ])
        class_list = sqlhepr.select_all_data("select * from  classes", [])
        sqlhepr.close_data()
        context = {}
        context['class_list'] = class_list
        context['result'] = result
        return render(request,"editorstudent.html",context)

def deletestudent(request):
    nid = request.GET.get('nid')
    sqlhepr = SqlHeper()
    sqlhepr.delete_data("delete from students where id=%s",[nid,])
    sqlhepr.commit_data()
    return redirect('/students/')

def classes(request):
    sqlhepr = SqlHeper()
    result = sqlhepr.select_all_data("select *  from classes",[])
    sqlhepr.close_data()
    context={}
    context['classes'] = result
    return render(request,'classes.html',context)

def addclass(request):
    sqlhepr = SqlHeper()
    if request.method == 'POST':
        data = request.POST.get('addclass')
        sqlhepr.insert_data("insert into classes (title) value(%s)", [data])
        sqlhepr.commit_data()
        sqlhepr.close_data()
        return redirect('/classes/')
    else:
        context = {}
        return render(request,'addclass.html',context)

def editorclass(request):
    nid=request.GET.get('nid')
    sqlhepr = SqlHeper()
    if request.method == "POST":
        date = request.POST.get('editorclass')
        sqlhepr.updata_data("update classes set title=%s where id=%s", [date,nid ])
        sqlhepr.commit_data()
        sqlhepr.close_data()
        return redirect('/classes/')

    else:
        result = sqlhepr.select_one_data("select id,title from classes where id=%s",[nid,])
        sqlhepr.close_data()
        context = {}
        context['editor_class'] = result
        return render(request,'editorclass.html',context)

def deleteclass(request):
    nid = request.GET.get('nid')
    sqlhepr = SqlHeper()
    sqlhepr.delete_data("delete from classes where id=%s", [nid, ])
    sqlhepr.commit_data()
    sqlhepr.close_data()
    return redirect('/classes/')

def modal_addclass(request):
    sqlhepr = SqlHeper()
    data = {}
    if request.method == 'POST':
        new_class = request.POST.get('modal_addclass')
        if new_class.strip() == '':
            data["status"] = 'error'
            data['message'] = '输入错误，请重新输入'
            return JsonResponse(data)
        else:
            sqlhepr.insert_data("insert into classes (title) value(%s)", [new_class])
            sqlhepr.commit_data()
            sqlhepr.close_data()
            data["status"] = 'ok'
            return JsonResponse(data)

def modal_editorclass(request):
    sqlhepr = SqlHeper()
    data = {}
    data['status'] = 'success'
    data['message'] = None
    try:
        nid = request.GET.get('nid')
        title = request.GET.get('title')
        if title.strip() != '':
            sqlhepr.updata_data("update classes set title=%s where id=%s", [title, nid])
            sqlhepr.commit_data()
            sqlhepr.close_data()
        else:
            data['status'] = 'error'
            data['message'] = '输出的内容不能为空'
    except Exception as e:
        data['message'] = e
    return JsonResponse(data)

def modal_deleteclass(request):
    sqlhepr = SqlHeper()
    nid = request.POST.get('nid')
    sqlhepr.delete_data("delete from classes where id=%s", [nid, ])
    sqlhepr.commit_data()
    sqlhepr.close_data()
    data={}
    data['status'] = 'success'
    return JsonResponse(data)

def modal_addstudent(request):
    sqlhepr = SqlHeper()
    context = {}
    try:
        studentname = request.POST.get('studentname')
        if studentname.strip() == '':
            context['status'] = 'error'
            context['message'] = '输入的学生姓名不能为空'
            return JsonResponse(context)
        class_id = request.POST.get('class_id')
        sqlhepr.insert_data("insert into students(name,class_id) value(%s,%s)",[studentname,class_id,])
        sqlhepr.commit_data()
        sqlhepr.close_data()
        context['status'] = 'success'
    except Exception as e:
        context['status'] = 'error'
        context['message'] = str(e)
    return JsonResponse(context)

def modal_editorstudent(request):
    sqlhepr = SqlHeper()
    try:
        student_id = request.POST.get('nid')
        student_name = request.POST.get('student_name')
        class_id = request.POST.get('class_id')
        sqlhepr.updata_data('update students set name=%s,class_id=%s where id=%s',[student_name,class_id,student_id])
        sqlhepr.commit_data()
        sqlhepr.close_data()
        context = {}
        context['status'] = 'success'
    except Exception as e:
        context['status'] = 'error'
        context['message'] = str(e)
    return JsonResponse(context)

def tearchs(request):
    sqlhepr = SqlHeper()
    tearchs_list = sqlhepr.select_all_data("""
    select tearch2class.id, tearchs.id as tid ,tearchs.tname,classes.title from tearch2class 
    left join tearchs on tearch2class.tearch_id=tearchs.id 
    left join classes on tearch2class.class_id=classes.id
    """,[])
    sqlhepr.close_data()
    res = {}
    for data in tearchs_list:
        tid = data['tid']
        if tid in res:
            res[tid]['titles'].append(data['title'])
        else:
            res[tid] = {"tid": data['tid'], 'name': data['tname'], 'titles': [data['title'], ]}

    context={}
    context['tearchs_list'] = res
    return render(request,'tearchs.html',context)

def add_tearch(request):
    sqlhepr = SqlHeper()
    if request.method == "POST":
        tearch_name = request.POST.get('add_tearchname')
        class_ids = request.POST.getlist('class_id')
        tearch_id = sqlhepr.lastrowid("insert into tearchs (tname) value(%s)",[tearch_name,])
        class_many_id = map(lambda x:(tearch_id,x),class_ids)
        sqlhepr.insert_many_data("insert into tearch2class (tearch_id,class_id) value(%s,%s)",class_many_id)
        sqlhepr.commit_data()
        sqlhepr.close_data()
        return redirect('/tearchs/')
    else:
        import pymysql
        conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='test',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select * from classes")
        class_list = cursor.fetchall()
        context = {}
        context['class_list'] = class_list
    return render(request,'add_tearch.html',context)

def editor_tearch(request):
    sqlhepr = SqlHeper()
    context = {}
    if request.method == 'POST':
        t_id = request.GET.get('t_id')
        #的到的是字符串
        t2c_id = request.POST.get('t_c_ids')
        # 转化为列表
        import re
        compile = re.compile('\d+')
        t2c_id = compile.findall(t2c_id)
        editor_class_ids = request.POST.getlist('editor_class_ids')
        t_name = request.POST.get('t_name')
        t_c = list(map(lambda x:(t_id,x),editor_class_ids))
        sqlhepr.updata_data("update tearchs set tname=%s where id=%s",[t_name,t_id])
        for i in t2c_id:
            sqlhepr.delete_data("delete from tearch2class where id=%s ",[i])
        sqlhepr.commit_data()
        sqlhepr.updata_many_data("insert  into tearch2class (tearch_id,class_id)value(%s,%s)",t_c)
        sqlhepr.commit_data()
        sqlhepr.close_data()
        return redirect('/tearchs/')
    else:
        tid = request.GET.get('tid')
        tearch_name = sqlhepr.select_one_data("select tname from tearchs where id=%s ",[tid])
        current_class_list = sqlhepr.select_all_data("select id ,class_id from tearch2class where tearch_id=%s",[tid])
        tearch_class_ids = list(map(lambda x:x['id'],current_class_list))
        current_class_ids = list(map(lambda x: x.get('class_id'),current_class_list))
        class_list = sqlhepr.select_all_data("select id,title from classes ",[])
        sqlhepr.close_data()
        context['tearch_name'] = tearch_name
        context['current_class_ids'] = current_class_ids
        context['class_list'] =  class_list
        context['tearch_class_ids'] = tearch_class_ids
        context['t_id'] = tid
        return render(request,'editor_tearch.html',context)
#对话框添加老师
def modal_add_tearch(request):
    context = {}
    if request.method == 'GET':
        import time
        time.sleep(1)
        sqlheper = SqlHeper()
        class_list = sqlheper.select_all_data("select id,title from classes",[])
        sqlheper.close_data()
        context['class_list'] = class_list
    else:
        try:
            t_name = request.POST.get('t_name')
            class_id_list =request.POST.getlist('class_id_list')
            sqlheper = SqlHeper()
            t_id = sqlheper.lastrowid("insert into tearchs (tname)value(%s)",[t_name,])
            t_c_id = list(map(lambda x:(t_id,x),class_id_list))
            sqlheper.insert_many_data("insert into tearch2class (tearch_id,class_id)value(%s,%s)",t_c_id)
            sqlheper.commit_data()
            sqlheper.close_data()
            context={}
            context['status'] = 'success'
        except Exception as e:
            context['status'] = 'error'
            context['message'] = str(e)
    return JsonResponse(context)
