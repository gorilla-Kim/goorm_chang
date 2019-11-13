from django.db import models

# Create your models here.

#프론트 부분에서 내용을 받을 수 있게 DB로 작성 -심세은
#거래처 리스트를 담고 있는 DB
class Intro(models.Model):
    client = models.CharField(max_length=50)
    def __str__(self):
        return self.client

#CEO 인사말을 담고 있는 DB
class About(models.Model):
    context = models.TextField()
    def __str__(self):
        return self.context

#보유하고 있는 주요 기계를 담고 있는 DB
class Service(models.Model):
    tech_name = models.CharField(max_length=500) #기계 이름
    tech_content = models.TextField() #기계 설명
    def __str__(self):
        return self.tech_name

#연락처를 담고 있는 DB
class Contact(models.Model):
    office = models.CharField(max_length = 50) #지사
    call = models.CharField(max_length=100) #전화번호
    pax = models.CharField(max_length=100) #팩스 
    email =models.EmailField(max_length=254) #이메일
    def __str__(self):
        return self.office