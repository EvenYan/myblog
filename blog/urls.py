"""
  Created by Even on 2018-10-14
"""
from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r"addpost", views.add_post, name="addpost"),

]
