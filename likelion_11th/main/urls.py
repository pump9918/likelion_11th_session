from django.urls import path
from .views import * # main 앱 내의 views.py를 사용하기 위한 코드
from django.contrib import admin

app_name = "main"
urlpatterns = [
    path('', mainpage, name="mainpage"),
    path('secondpage/', secondpage, name="secondpage"),
    path('thirdpage/', thirdpage, name="thirdpage"),
    path('new/', new, name="new"), #new 페이지 url 연결
    path('create/', create, name="create"), #create 생성페이지 url 연결
    path('<int:id>', detail, name="detail"), #id에 부합하는 detail페이지로 연결
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]