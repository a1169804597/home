import string
import random
import time
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import JsonResponse
from .forms import LoginForm, RegForm,ChangeNicknameForm,BindEmailForm,ChangePasswordForm,ForgotPasswordForm
from .models import Profile
from django.core.mail import send_mail

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'user/login.html', context)

def login_for_medal(request):
    login_form = LoginForm(request.POST)
    data = {}
    if login_form.is_valid():
        user = login_form.cleaned_data['user']
        auth.login(request, user)
        data['status'] = 'SUCCESS'
    else:
        data['status'] = 'ERROR'
    return JsonResponse(data)

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST,request=request)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            # 创建用户
            user = User.objects.create_user(username, email, password)
            del request.session['register_code']
            user.save()
            # 登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'user/register.html', context)

def user_info(request):

    context={}
    return render(request,'user/user_info.html',context)

def login_out(request):
    auth.logout(request)
    context={}
    return redirect( reverse('home'))

def change_nickname(request):
    redirect_to = request.GET.get('from',reverse('home'))
    if request.method == 'POST':
        nickname_form=ChangeNicknameForm(request.POST,user=request.user)
        if nickname_form.is_valid():
            nickname_new=nickname_form.cleaned_data['nickname_new']
            profile,created = Profile.objects.get_or_create(user=request.user)
            profile.nickname=nickname_new
            profile.save()
            return redirect(redirect_to)
    else:
        nickname_form=ChangeNicknameForm()
    context={}
    context['page_text']='修改昵称'
    context['submit_text']='修改'
    context['form']=nickname_form
    context['return_back_url']=redirect_to
    return render(request,'form.html',context)

def bind_email(request):
    redirect_to=request.GET.get('from',reverse('home'))
    if request.method == 'POST':
        email_form=BindEmailForm(request.POST,request=request)
        if email_form.is_valid():
            email=email_form.cleaned_data['email']
            request.user.email=email
            del request.session['bind_code']
            request.user.save()
            return redirect(redirect_to)
    else:
        email_form=BindEmailForm()
    context={}
    context['page_text']='绑定邮箱'
    context['submit_text']='绑定'
    context['form']=email_form
    context['return_back_url']=redirect_to
    return render(request,'user/bind_email.html',context)

def send_verification_code(request):
    email=request.GET.get('email',)
    data={}
    if email !='':
        code=''.join(random.sample(string.ascii_letters+string.digits,4))
        now = int(time.time())
        send_code_time = request.session.get('send_code_time', 0)
        if now - send_code_time < 30:
            data['status'] = 'ERROR'
        else:
            code_name=request.GET.get('vericode','')
            send_email_type=request.GET.get('send_email_type','')
            request.session[code_name]=code
            request.session['send_code_time'] = now
            send_mail(
                send_email_type,
                '验证码：%s' % code,
                '1480244514@qq.com',
                [email],
                fail_silently=False,
            )
            data['status']= 'SUCCESS'
    else:
        data['status']='ERROR'
    return JsonResponse(data)

def change_password(request):
    redirect_to = request.GET.get('from', reverse('home'))
    if request.method=='POST':
        change_password_form = ChangePasswordForm(request.POST,request=request)
        if change_password_form.is_valid():
            new_password=change_password_form.cleaned_data['new_password']

            user=request.user
            user.set_password(new_password)
            user.save()
    else:
        change_password_form = ChangePasswordForm()
    context={}
    context['page_text']='修改密码'
    context['submit_text']='修改'
    context['form']=change_password_form
    context['return_back_url']=redirect_to
    return render(request,'form.html',context)

def forgot_password(request):
    redirect_to = request.GET.get('from', reverse('home'))
    if request.method == 'POST':
        forgot_password_form = ForgotPasswordForm(request.POST,request=request)
        if forgot_password_form.is_valid():
            del request.session['forgot_email_code']
            new_password=forgot_password_form.cleaned_data['new_password']
            user=request.user
            user.set_password(new_password)
            user.save()
            return redirect(redirect_to)
    else:
        forgot_password_form= ForgotPasswordForm()
    context={}
    context['page_text'] = '忘记密码'
    context['submit_text'] = '重置'
    context['form'] = forgot_password_form
    context['return_back_url'] = redirect_to
    return render(request,'user/forgot_password.html',context)
