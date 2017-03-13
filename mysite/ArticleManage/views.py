from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from .forms import ArticleColumnForm, ArticlePostForm
from .models import ArticleColumn, ArticlePost


# Create your views here.

@login_required(login_url='/account/login')
@csrf_exempt
def article_column(request):
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(user_id=request.user.id)
        column_form = ArticleColumnForm()
        return render(request, "ArticleManage/column/article_column.html",
                      {"columns": columns, 'column_form': column_form})

    if request.method == "POST":
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user, column=column_name)
            return HttpResponse('1')


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def rename_article_column(request):
    column_name = request.POST["column_name"]
    column_id = request.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.column = column_name
        line.save()
        return HttpResponse("1")
    except:
        return HttpResponse("0")


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST['column_id']
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("0")


@login_required(login_url='/account/login')
@csrf_exempt
def article_post(request):
    if request.method == "POST":
        # 首先获取表单的数据,然后验证
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            # 获取表单数据
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()
                return HttpResponse("1")
            except:
                return HttpResponse('2')
        else:
            return HttpResponse("3")
    else:
        article_post_form = ArticlePostForm()
        article_columns = request.user.article_column.all()
        return render(request, "ArticleManage/article/article_post.html",
                      {"article_post_form": article_post_form, "article_columns": article_columns})


@login_required(login_url='/account/login')
@csrf_exempt
def article_list(request):
    articles = ArticlePost.objects.filter(author=request.user)
    return render(request, "ArticleManage/article/article_list.html", {"articles": articles})


@login_required(login_url='/account/login')
def article_detail(request, id, slug):
    article = get_object_or_404(ArticlePost, id=id, slug=slug)
    return render(request, "ArticleManage/article/article_detail.html", {"article": article})


@login_required(login_url="/account/login")
@require_POST
@csrf_exempt
def del_article(request):
    article_id = request.POST['article_id']
    try:
        article = ArticlePost.objects.get(id=article_id)
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")


@login_required(login_url="/account/login")
@csrf_exempt
def redit_article(request, article_id):
    if request.method == "GET":
        article_columns = request.user.article_column.all()
        article = ArticlePost.objects.get(id=article_id)
        this_article_form = ArticlePostForm(initial={"title": article.title})
        this_article_column = article_column
        return render(request, "ArticleManage/article/redit_article.html",
                      {"this_article_form": this_article_form, "this_article_column": this_article_column,
                       "article_columns": article_columns})
    else:
        redit_articles = ArticlePost.objects.get(id=article_id)
        try:
            redit_articles.title = request.POST['title']
            redit_articles.column = request.user.article_column.get(id=request.POST['column_id']),
            redit_articles.body = request.POST['body'],
            redit_articles.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")
