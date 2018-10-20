import hashlib

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from user.models import UserInfo


def index(request):
    username = request.session['username']
    context = {"username": username}
    return render(request, 'user/index.html', context=context)


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        passwd = gen_sec_passwd(passwd)
        user = UserInfo.objects.filter(username=username, passwd=passwd)
        if user:
            request.session['username'] = username
            response = redirect(reverse('user:index'))
            return response
        else:
            return HttpResponse("用户名错误或者密码错误")


    return render(request, 'user/login.html')


def gen_sec_passwd(passwd):
    md5 = hashlib.md5()
    md5.update(passwd.encode())
    return md5.hexdigest()


def register(request):
    username = request.POST.get("username")
    passwd = request.POST.get("password")
    confirm_passwd = request.POST.get("confirm_password")
    email= request.POST.get("email")
    if passwd==confirm_passwd and len(passwd) >= 8:
        user = UserInfo()
        passwd = gen_sec_passwd(passwd)
        confirm_passwd = gen_sec_passwd(confirm_passwd)
        user.username = username
        user.passwd = passwd
        user.confirm_passwd = confirm_passwd
        user.email = email
        user.save()
        print("加密后的密码是：%s"%passwd)

        return HttpResponse("注册成功")
    print("*"*50)
    print(username, passwd, confirm_passwd, email)

    return HttpResponse("密码输入不符合规范")