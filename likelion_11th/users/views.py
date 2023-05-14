from django.shortcuts import render, redirect
from main.models import Post

def mypage(request):
    if request.method == 'GET':
        # posts = Post.objects.all() #변수 posts에 Post의 모든 객체 내용을 저장
        posts = Post.objects.filter(user = request.user)
        return render(request, 'users/mypage.html', {'posts':posts}) # Read 기능 위한 작업