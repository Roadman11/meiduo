from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from django.views import View
from django.http import JsonResponse

from users.models import User


# GET /usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/
class UsernameCountView(View):
    def get(self, request, username):
        """判断注册用户名是否重复"""
        # ① 查询数据库判断username是否存在
        try:
            count = User.objects.filter(username=username).count()
        except Exception as e:
            return JsonResponse({'code': 400,
                                 'message': '操作数据库失败!'})

        # ② 返回响应数据
        return JsonResponse({'code': 0,
                             'message': 'OK',
                             'count': count})


class MobileCountView(View):
    def get(self, request, mobile):
        """判断注册手机号是否重复"""
        # ① 查询数据库判断mobile是否存在
        try:
            count = User.objects.filter(mobile=mobile).count()
        except Exception as e:
            return JsonResponse({'code': 400,
                                 'message': '操作数据库失败!'})

        # ② 返回响应数据
        return JsonResponse({'code': 0,
                             'message': 'OK',
                             'count': count})