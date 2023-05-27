from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, null=True) #제목 필드
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE) #작성자 필드
    address = models.CharField(max_length=200, null=True) #장소(주소) 필드
    weather = models.CharField(max_length=100, default = '', null=True) #날씨 필드, 나중에 추가해서 마이그레이션 위해 디폴트 추가
    pub_date = models.DateTimeField() #작성 시간 필드
    body = models.TextField() #게시글 필드
    image = models.ImageField(upload_to="blog/", blank=True, null=True) #이미지 필드
    # user = models.ForeignKey(User, on_delete = models.CASCADE) # 게시물에 유저 id 저장
    #tag 필드추가
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    # related_name='posts'인 이름은 어떤 해시태그가 들어가는 포스트 알려줘 =>에서 포스트에 해당
    
    def __str__(self):
        return self.title #데이터를 호출하면 대푯값으로 데이터의 title이 나오게 됨
    
    def summary(self):
        return self.body[:30] #내용이 너무길 때 앞부분 30글자만 보이도록 slicing
    

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post.title + " : " + self.content[:20]