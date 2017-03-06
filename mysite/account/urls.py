    # -*- coding:utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import password_change

from .import views

from django.conf import settings
#第二个参数为views 中的函数名字
urlpatterns=[
    url(r'^login/$',views.user_login,name="user_login"),
    url(r'^logout/$',views.logout,name='user_logout'),
    url(r'^register/$',views.register,name="user_register"),
    url(r'^password_change/$',password_change,name="password_change")
]