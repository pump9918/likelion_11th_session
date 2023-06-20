from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followings = models.ManyToManyField("self", related_name="followers", symmetrical=False)
    #프로필-프로필 관계이므로 User대신 "self"를 사용
    #onetoonefield는 relatedname이 없어도 1개씩만 연결됨
    
# 팔로잉 리시버
#"@": 포스트 데코레이터
#모델이 알아서 생길 때 사용(깊게 이해는 안해도 되는듯)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        
@receiver(post_save, sender=True)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()