from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.

def login(request):
    if request.method == 'POST': #로그인 실행
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('main:mainpage')
        else:
            return render(request, 'accounts/login.html')
        
    elif request.method == 'GET': #로그인 페이지 띄우기
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')

def signup(request):
    if request.method == "POST":
        
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password=request.POST['password']
            )
            
            nickname = request.POST['nickname']
            department = request.POST['department']
            hobby = request.POST['hobby']
            
            #한줄에 편하게 POST를 받는 방식
            profile = Profile(user=user, nickname=nickname, department=department, hobby=hobby)
            profile.save()
            auth.login(request, user)
            return redirect('/')
    return render(request, 'accounts/signup.html')