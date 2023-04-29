from django.shortcuts import render, redirect, get_object_or_404 
# render: 템플릿 불러옴 / redirect: url로 이동 / get_object_or_404: 객체가 있으면 가져오고 없으면 404에러 띄우기
from .models import Post
from django.utils import timezone #django 기본 제공 시간관련 기능

# Create your views here.
def mainpage(reqeust):
    posts = Post.objects.all() #변수 posts에 Post의 모든 객체 내용을 저장
    return render(reqeust, 'main/mainpage.html', {'posts':posts}) # Read 기능 위한 작업

def secondpage(request):
    return render(request, 'main/secondpage.html')

def thirdpage(request):
    return render(request, 'main/thirdpage.html')

def new(request): #앞의 new.html을 띄우는 함수
    return render(request, 'main/new.html')

def create(request): #포스트 생성(CRUD 중 C)
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.address = request.POST['address']
    new_post.weather = request.POST['weather']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    
    new_post.save()
    
    return redirect('detail', new_post.id) #새로 생성한 post id와함께 detail 페이지로 이동

def detail(request, id): #id에 원하는 게시글의 id 값을 넣어 detail 함수를 실행
    post = get_object_or_404(Post, pk = id) #Post와 id를 받아서 전송 or 오류표시
    return render(request, 'main/detail.html', {'post':post}) # id에 부합하는 게시물 1개씩 관리(detail 페이지)
    # pk(Primary Key): 각 객체를 구분해주는 키 값