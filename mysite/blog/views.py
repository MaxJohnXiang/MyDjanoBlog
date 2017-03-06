from django.shortcuts import render
from .models import BlogArticle
# Create your views here.

def blog_title(request):
    blogs=BlogArticle.objects.all()
    return render(request,'blog/titles.html',{"blogs":blogs})


def blog_article(request,article_id):
    article=BlogArticle.objects.get(id=article_id)
    author=article.author.username
    time=article.publish
    title=article.title
    content=article.body
    #传回数据给html 页面,
    return render(request,'blog/content.html',{"author":author,"time":time,"title":title,"content":content})
