"""likelion_11th URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name="mainpage"),
    path('secondpage/', views.secondpage, name="secondpage"),
    path('thirdpage/', views.thirdpage, name="thirdpage"),
    path('new/', views.new, name="new"), #new 페이지 url 연결
    path('create/', views.create, name="create"), #create 생성페이지 url 연결
    path('<int:id>', views.detail, name="detail"), #id에 부합하는 detail페이지로 연결
]
