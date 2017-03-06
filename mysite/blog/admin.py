from django.contrib import admin
from .models import BlogArticle
# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display=('title','author','publish')#显示字段
    list_filter=('publish','author') #筛选项目
    search_fields =('title','body')#
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['publish','author']

admin.site.register(BlogArticle,BlogArticlesAdmin)
