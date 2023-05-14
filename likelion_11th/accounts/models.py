from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model): #기존 allauth에서 제공하는건 User에서, 개인적으로 추가하는 필드는 Profile 클래스로
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    department = models.TextField(null=True, max_length=30)
    hobby = models.TextField(null=True, max_length=20)