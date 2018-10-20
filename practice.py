"""
  Created by Even on 2018-10-20
"""
import datetime
import os
import random
import time

import django
import requests
from django.db.models import Avg, Sum, F, Q

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblog.settings")
django.setup()
from django.db import connection

from blog.models import *
post = Post.objects.all()

# print(post)


post1 = Post.objects.filter(id__gt=10)
# print(post1.order_by("title"))
# for post in Post.objects.all():
#     print(post)
#
# print(connection.queries)


# 去重
# qs = Post.objects.all().values_list('title').distinct()
# print(qs)

#

sum_views = Post.objects.aggregate(Sum("id"))
# print(sum_views)

# F对象
post = Post.objects.filter(id__gte=F("views"))
# print(post)

# F对象的数字运算
post1 = Post.objects.get(id=3)
# 在数据库中+100
# post1.views = F("views") + 100
# python内存计算
# post1.views += 100
# post1.save()

post_list = Post.objects.filter(Q(id__gte=10)|Q(views__gt=105))
for post in post_list:
    print(post.id)
    print(post.views)
    print("*"*50)



# from lxml import etree


from blog.models import *


# # User-Agent
# header_list = [
#     {"User-Agent":"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"},
#     {"User-Agent":"Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50"},
#     {"User-Agent":"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)"},
#     {"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1"},
#     {"User-Agent":"Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1"},
#     {"User-Agent":"Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11"},
#     {"User-Agent":"Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11"},
#     {"User-Agent":"Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TencentTraveler4.0)"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser)"},
#     {"User-Agent":"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)"},
# ]
#
#
# def save_post(**kwargs):
#     title = kwargs.get('title')
#     body = kwargs.get('body')
#     created_time = kwargs.get('created_time')
#     modified_time = kwargs.get('modified_time')
#     excerpt = kwargs.get('expcerpt')
#     post = Post()
#     post.title = title
#     post.body = body
#     post.created_time = created_time
#     post.modified_time = modified_time
#     post.excerpt = body[:54]
#     post.views = random.randint(100, 200)
#     print(post.created_time, post.modified_time)
#     post.save()
#     print(Post.objects.last().created_time)
#
#
# def get_data(url):
#     """
#     获取文章内容
#     //div[@class='detail mb10']//div[@class='detail-c']/p
#     获取文章标题
#     //div[@class='detail mb10']//div[@class='detail-t fix']/h1
#     """
#
#
#     # 获取文章标题和正文
#     headers = random.choice(header_list)
#     response = requests.get(url, headers=headers)
#     # print(response.content.decode())
#     html_etree = etree.HTML(response.content.decode())
#     title = ""
#     title = ""
#     try:
#         p_list = html_etree.xpath("//div[@class='detail mb10']//div[@class='detail-c']/p/text()")
#         body = "\n".join(p_list)
#         title = html_etree.xpath("//div[@class='detail mb10']//div[@class='detail-t fix']/h1/text()")[0]
#     except Exception as e:
#         pass
#
#     # print(body)
#     # print(title)
#     return title, body
#
#
# def main():
#     for i in range(200):
#         url = "".join(["https://mingyan.chazidian.com/mingyan45", str(random.randrange(210, 500))])
#         title, body = get_data(url)
#         if title=="" and title=="":
#             continue
#         else:
#             year = random.randrange(1999, 2018)
#             month = random.randrange(1, 12)
#             day = random.randrange(1, 28)
#             microsecond = 100000
#             created_time = datetime.datetime(year=year, month=month, day=day, microsecond=microsecond)
#             modified_time = datetime.datetime(year, month, day, microsecond=microsecond)
#             print(created_time, modified_time)
#             save_post(title=title, body=body, created_time=created_time, modified_time=modified_time)
#             time.sleep(random.randrange(3))
#
#
# if __name__ == '__main__':
#     main()


# requests
# lxml