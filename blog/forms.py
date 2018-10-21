"""
  Created by Even on 2018-10-21
"""
from django import forms
from captcha.fields import CaptchaField

class UserInfo(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # error_messages包含验证码错误的信息的一个字典
    myfield = CaptchaField(error_messages={"invalid": "pytpyt"})
