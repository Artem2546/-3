from django.contrib import admin
from articles.models import Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_date')
admin.site.register(Article, ArticleAdmin)
# Register your models here.