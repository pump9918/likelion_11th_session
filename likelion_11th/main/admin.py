from django.contrib import admin
from .models import Post, Comment, Tag

# Register your models here.

admin.site.register(Post) #admin에 Post클래스 등록
admin.site.register(Comment)
admin.site.register(Tag)