from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200) #제목 필드
    writer = models.CharField(max_length=100) #작성자 필드
    address = models.CharField(max_length=200) #장소(주소) 필드
    weather = models.CharField(max_length=100, default = '') #날씨 필드, 나중에 추가해서 마이그레이션 위해 디폴트 추가
    pub_date = models.DateTimeField() #작성 시간 필드
    body = models.TextField() #게시글 필드
    
    def __str__(self):
        return self.title #데이터를 호출하면 대푯값으로 데이터의 title이 나오게 됨
    
    def summary(self):
        return self.body[:30] #내용이 너무길 때 앞부분 30글자만 보이도록 slicing