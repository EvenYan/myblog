"""
  Created by Even on 2018-10-14
"""
from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r"addpost", views.add_post, name="addpost"),
    url(r"(\d+)", views.index, name="index"),
    url(r"posts/(\d+)", views.get_post, name="posts"),
    url(r"detail/(?P<num>\d+)", views.detail, name="detail"),
    url(r"info", views.get_form, name="info"),
    url(r"tmp", views.tmp, name="tmp"),
    url(r"page/(\d+)", views.page, name="page"),
    url(r"register", views.register_form, name="register_form"),
    url(r"^$", views.home, name="home"),

]
