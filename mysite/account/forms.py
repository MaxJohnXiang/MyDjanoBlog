# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


#实现用户注册和用户登录都非常的类似,  要写一个表单 就是利用原有 的数据库  或者说django 默认的用户模型
class RegistrationForm(forms.ModelForm):
    password=forms.CharField(label="password",widget=forms.PasswordInput)
    password=forms.CharField(label="Confirm password",widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=("username","email")

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password']!=cd['password2']:
            raise forms.ValidationError("两次输入密码不一致")
        return cd['password2']



class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=("phone","birth")

