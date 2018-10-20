# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=100)
    views = models.PositiveIntegerField(default=666)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    author = models.ForeignKey(User)

    def __str__(self):
        return self.title
