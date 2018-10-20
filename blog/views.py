# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse

from blog.models import Post


def index(request):
    print("request path:", request.path)
    print("request method:", request.method)
    print("request encoding:", request.encoding)
    print("request Cookies:", request.COOKIES)
    print("request get:", request.GET)
    # request.GET['name']
    # request.GET.get('name', "陌生人")
    print("request post:", request.POST)
    print("request get host:", request.get_host())

    username = request.POST.get("username")
    passwd = request.POST.get("passwd")
    print("用户名", username)
    print("密码:", passwd)

    response = HttpResponse()
    response.content = "你好，这是content定义的内容"
    response.status_code = 302
    response.write("这是write方法写入的数据")
    response.set_cookie('name', 'alice', max_age=30)

    # 位置参数的反向解析
    # return redirect(reverse('blog:detail', args=(10,))
    # 关键字参数的反向解析
    return redirect(reverse('blog:detail', kwargs={"num": 10}))


def get_form(requset):
    return render(requset, 'blog/form.html')


def get_post_list(request):
    post_list = Post.objects.all()
    context = {"post_list": post_list}

    return render(request, 'blog/post_list.html', context=context)


def add_post(request):
    post = Post()
    num = random.randrange(100)
    post.title = "第%s文章" % num
    post.body = "body of %s" % num
    post.save()
    return HttpResponse("Hello Django!")


def detail(request, num):
    # a = 10 / 0
    post = get_object_or_404(Post, id=num)
    context = {"post": post}
    return render(request, 'blog/detail.htm', context=context)


def tmp(request):
    post_list = Post.objects.all()
    name = ""
    context = {"post_list": post_list, 'name': name, 'html': "<script>alert('你好！')</script>"}
    # return HttpResponse("<h1 style='color:red'>标题1</h1>")
    return render(request, 'page.html', context=context)