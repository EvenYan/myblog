# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class CountManager(models.Manager):
    def title_count(self, kw):
        return self.filter(title__contains=kw)


class SecretManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(excerpt="secret")


class NormalManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().exclude(excerpt="secret")



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


    my_objects = models.Manager()
    count_objects = CountManager()
    secret_objects = SecretManager()
    normal_objects = NormalManager()

    def __str__(self):
        return self.title
