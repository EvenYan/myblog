# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractYear
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from markdown import markdown

from blog.forms import UserInfo
from blog.models import Post, Category


def get_recent_post(num=5):
    recent_post = Post.my_objects.all().order_by('-created_time')[:num]
    return recent_post


def get_category():
    cates = Category.objects.annotate(num_count=Count("post")).filter(num_count__gt=0)
    return cates


def get_date():
    # dates = Post.my_objects.annotate(month=ExtractMonth("created_time"), year=ExtractYear("created_time")).annotate(total=Count("*")).filter(total__gt=0).values("month", "year", "total").order_by("-year", "-month")
    dates = Post.my_objects.annotate(month=ExtractMonth('created_time'), year=ExtractYear('created_time'), ).order_by('-month').values('month', 'year').annotate(total=Count('*')).values('month', 'year', 'total').order_by('-year','-month')
    print(dates.query)
    return dates


def index(request, num):
    post_list = Post.normal_objects.all()
    paginator = Paginator(post_list, 10)
    page = paginator.page(num)
    page_range = paginator.page_range
    page_list = page.object_list

    recent_post = get_recent_post()
    cates = get_category()
    dates = get_date()
    context = {'page_list': page_list, 'recent_post': recent_post, 'cates': cates, 'dates': dates, 'page': page, 'page_range': page_range}
    return render(request, 'blog/index.html', context)


def home(request):
    return redirect(reverse('blog:index', args=(1, )))


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
    post.body = markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.views += 1
    print(post.views)
    post.save()
    context = {"post": post}
    return render(request, 'blog/detail.htm', context=context)


def tmp(request):
    post_list = Post.objects.all()
    name = ""
    context = {"post_list": post_list, 'name': name, 'html': "<script>alert('你好！')</script>"}
    # return HttpResponse("<h1 style='color:red'>标题1</h1>")
    return render(request, 'page.html', context=context)


def page(request, num):
    post_list = Post.my_objects.all()
    paginator = Paginator(post_list, 10)
    page = paginator.page(num)
    page_range = paginator.page_range
    page_list = page.object_list

    context = {"page_list": page_list, 'page': page, 'page_range': page_range}
    return render(request, 'blog/page.html', context=context)


def register_form(request):
    register_form = UserInfo()
    context = {"register_form": register_form}
    return render(request, 'blog/register_form.html', context)





def get_post(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()

    context = {"post": post}
    return render(request, 'blog/detail.html', context)