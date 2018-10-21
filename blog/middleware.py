"""
  Created by Even on 2018-10-21
"""

# blog/middleware.py
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware1(MiddlewareMixin):
    def process_request(self, request):
        print("执行MyMiddleware1的process_request方法！")
        # return HttpResponse("提前返回")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print("执行MyMiddleware1的process_view方法！")

    def process_response(self, request, response):
        print("执行MyMiddleware1的process_response方法！")
        return response

    def process_exception(self, request, exception):
        print("执行MyMiddleware1的process_exception方法！")

    def process_template_response(self, request, response):
        print("执行MyMiddleware1的process_template_response方法！")


class MyMiddleware２(MiddlewareMixin):
    def process_request(self, request):
        print("执行MyMiddleware2的process_request方法！")
        # return HttpResponse("提前返回")

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print("执行MyMiddleware２的process_view方法！")

    def process_response(self, request, response):
        print("执行MyMiddleware２的process_response方法！")
        return response

    def process_exception(self, request, exception):
        print("执行MyMiddleware2的process_exception方法！")

    def process_template_response(self, request, response):
        print("执行MyMiddleware２的process_template_response方法！")


block_list = ["172.16.4.22"]

class BlockIP(MiddlewareMixin):

    def process_response(self, request, response):
        if request.META['REMOTE_ADDR'] in block_list:
            print(request.META['REMOTE_ADDR'])
            response.write("IP被限制")
        print(request.META['REMOTE_ADDR'])
        return response
