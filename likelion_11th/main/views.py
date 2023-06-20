from django.shortcuts import render, redirect, get_object_or_404 
# render: 템플릿 불러옴 / redirect: url로 이동 / get_object_or_404: 객체가 있으면 가져오고 없으면 404에러 띄우기
from .models import Post
from django.utils import timezone #django 기본 제공 시간관련 기능
from .models import *

# Create your views here.
def mainpage(request):
    posts = Post.objects.all() #변수 posts에 Post의 모든 객체 내용을 저장
    return render(request, 'main/mainpage.html', {'posts':posts}) # Read 기능 위한 작업


def secondpage(request):
    return render(request, 'main/secondpage.html')


def thirdpage(request):
    return render(request, 'main/thirdpage.html')


def new(request): #앞의 new.html을 띄우는 함수
    return render(request, 'main/new.html')


def create(request): #포스트 생성(CRUD 중 C)
    if request.user.is_authenticated:
        new_post = Post()
        new_post.title = request.POST['title']
        new_post.writer = request.user
        new_post.address = request.POST['address']
        new_post.weather = request.POST['weather']
        new_post.pub_date = timezone.now()
        new_post.body = request.POST['body']
        new_post.image = request.FILES.get('image')
        
        new_post.save()
        #html로 정보를 받고 request로 views.py 정보가 넘어오면 자동으로 id가 부여됨
        words = new_post.body.split(' ')
        tag_list = []
        for w in words:
            if len(w)>0:
                if w[0] == '#':
                    tag_list.append(w[1:])
        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t) #이미 있는 태그면 함께 사용, 없으면 생성하는 함수
            #boolean은 실제로는 사용을 안하지만 get_or_create에서 반환하는 2개의 값중 하나를 받기 위해(오류를 방지)
            new_post.tags.add(tag.id)
        return redirect('main:detail', new_post.id)
    #로그인 안했으면? 로그인 하러가기
    else:
        return redirect('accounts:login')


def detail(request, id): #id에 원하는 게시글의 id 값을 넣어 detail 함수를 실행
    post = get_object_or_404(Post, pk = id) #Post와 id를 받아서 전송 or 오류표시
    
    if request.method == 'GET': #그냥 블로그를 들어가는거
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html',{
            'post' : post,
            'comments' : comments,
        })
    elif request.method == "POST": #new.html을 통해 내용을 "보낸 거"
        new_comment = Comment()
        new_comment.post = post # 이 detail 함수의 게시물'post'
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.pub_date = timezone.now()
        new_comment.save()
        return redirect('main:detail', id)
    
    return render(request, 'main/detail.html', {'post':post}) # id에 부합하는 게시물 1개씩 관리(detail 페이지)
    # pk(Primary Key): 각 객체를 구분해주는 키 값

    
def edit(request, id):
    edit_post = Post.objects.get(id=id)
    return render(request, 'main/edit.html', {'post': edit_post})


def update(request, id):
    post = get_object_or_404(Post, pk = id)
    if request.user.is_authenticated:
        update_post = Post.objects.get(id=id)
        update_tags = Tag.objects.filter(posts=post)
        if request.user == update_post.writer:
            update_post.title = request.POST['title']
            update_post.writer = request.user
            update_post.address = request.POST['address']
            update_post.weather = request.POST['weather']
            update_post.pub_date = timezone.now()
            update_post.body = request.POST['body']
            update_post.image = request.FILES.get('image', update_post.image)
                        
            update_tags.delete()
            words = update_post.body.split(' ')
            tag_list = []
            for w in words:
                if len(w)>0:
                    if w[0] == '#':
                        tag_list.append(w[1:])
            for t in tag_list:
                tag, boolean = Tag.objects.get_or_create(name=t)
                update_post.tags.add(tag.id)
            update_post.save()
            return redirect('main:detail', update_post.id)                
    else:
        return redirect('accounts:login')


def delete(request, id):
    if request.user.is_authenticated:
        delete_post = Post.objects.get(id=id)
        if request.user == delete_post.writer:   
            delete_post.delete()
            return redirect('main:mainpage')
        return redirect('main:mainpage')
    else:
        return redirect('main:mainpage')


def comment_delete(request, comment_id):
    if request.user.is_authenticated:
        comment = Comment.objects.get(id = comment_id)
        post = comment.post
        if request.user == comment.writer:
            comment.delete()
            return redirect('main:detail', post.id)
        return redirect('main:mainpage')
    else:
        return redirect('main:mainpage')
    
    
# 모든 tag 리스트를 볼 수 있는 페이지 구현
def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag_list.html', {
        'tags':tags,
    })


# 태그 선택 시 해당 태그가 포함된 게시물 보는 기능 구현
def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag_posts.html', {
        'tag':tag,
        'posts':posts,
    })
    
#like 함수
def likes(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
    return redirect('main:detail', post.id)
