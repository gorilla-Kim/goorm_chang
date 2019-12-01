from django.db import models
# Create your models here.


class Board_Category(models.Model):
    name = models.CharField(max_length=20)    # 게시판 카테고리 이름
    
    admin_option = models.BooleanField(default=False) # 관리자만 확인하기 옵션 기능
    created_at = models.DateTimeField(auto_now_add=True)    # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True)    # 해당 레코드 갱신시 현재 시간 자동저장
    
    def __str__(self):
        return self.name
    
    
class Board(models.Model):
    board_category = models.ForeignKey(Board_Category, on_delete=models.CASCADE) # board category
    subject = models.CharField(max_length=20) # 제목
    email = models.EmailField() # user이메일
    pwd = models.CharField(max_length=20) # user pw
    content = models.TextField()    # 게시글 내용
    
    hit = models.IntegerField(default=0)    # 조회수 
    admin_option = models.BooleanField(default=False) # 관리자만 확인하기 옵션 기능
    created_at = models.DateTimeField(auto_now_add=True)    # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True)    # 해당 레코드 갱신시 현재 시간 자동저장
    ifmodify = models.CharField(max_length=2, default="n")
    def __str__(self):
        return self.subject

    def getNickName(self):
        emailSplit = self.email.split('@')
        return emailSplit[0]
    
    def getYMD(self):
        time = self.created_at.strftime('%Y-%m-%d')
        return time
    
    def getSubject(self):
        sub = self.subject
        if(len(self.subject)>17):
            sub = self.subject[0:17]+" ..."
        return sub
