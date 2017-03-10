from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn

# Create your views here.

@login_required(login_url='/account/login')
def article_column(request):
    columns=ArticleColumn.objects.filter(user_id=request.user.id)
    return render(request,"ArticleManage/column/article_column.html",{"columns":columns})