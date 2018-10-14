# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog.models import Post


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


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {"post": post}
    return render(request, 'blog/detail.htm', context=context)
