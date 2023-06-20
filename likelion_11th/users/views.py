from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.models import User
from main.models import Post
from .models import UserProfile


def mypage(request, id):
    user = get_object_or_404(User, pk=id)
    context = {
        'user':user,
        'posts':Post.objects.filter(writer=user),
        'followings' : user.userprofile.followings.all(),
        'followers' : user.userprofile.followers.all(),
    }
    return render(request, 'users/mypage.html', context)

def follow(request, id):
    user = request.user
    followed_user = get_object_or_404(User, pk=id) #상대방
    is_follower = user.userprofile in followed_user.userprofile.followers.all()
    #followers: related
    #followed_user: 내가 팔로우하는 한 사람
    if is_follower:
        user.userprofile.followings.remove(followed_user.userprofile)
    else:
        user.userprofile.followings.add(followed_user.userprofile)
    
    return redirect('users:mypage', followed_user.id)