# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Post


def add_post(request):
    post = Post()
    num = random.randrange(100)
    post.title = "第%s文章" % num
    post.body = "body of %s" % num
    post.save()
    return HttpResponse("Hello Django!")