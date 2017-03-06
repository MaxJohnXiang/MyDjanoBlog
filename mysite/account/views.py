from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .forms import User,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegistrationForm
# Create your views here.

def user_login(request):
    if request.method=="POST":
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user:
                login(request,user)
                return HttpResponse("Wellcome you. You have been authenticated successfully")
            else:
                return HttpResponse("Sorry, You password or username is not correct")
        else:
            return HttpResponse("Invalid Login")

    if request.method=="GET":
        login_form=LoginForm()
        return render(request,"account/login.html",{"form":login_form})

def logout(request):
    auth.logout(request)
    return render(request,"account/logout.html")


def register(request):
    if request.method=="POST":
        user_form=RegistrationForm(request.POST)
        userprofile_form=UserProfileForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile=userprofile_form.save(commit=False)
            new_profile.user=new_user
            new_profile.save()
            return HttpResponse("成功注册!")
        else:
            return HttpResponse("对不起,注册失败")
    else:
        #假如是get 请求,这个时候是请求显示表单, 所以返回一个渲染后的html
        user_form=RegistrationForm()
        userprofile_form=UserProfileForm()
        return render(request,"account/register.html",{"form":user_form,"profile":userprofile_form})


