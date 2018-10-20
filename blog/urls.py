"""
  Created by Even on 2018-10-14
"""
from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r"addpost", views.add_post, name="addpost"),
    url(r"^$", views.index, name="index"),
    url(r"posts", views.get_post_list, name="posts"),
    url(r"detail/(?P<num>\d+)", views.detail, name="detail"),
    url(r"info", views.get_form, name="info"),

]
