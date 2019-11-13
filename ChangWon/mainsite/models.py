from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

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
    
# mainsite 포트폴리오 정보 
class Portfolio(models.Model):
    image = models.ImageField(upload_to="portfolio")
    image_thumbnail = ImageSpecField(
        source = 'image',            # 원본 ImageField 명
        processors = [ResizeToFill(960, 720)], # 사이즈 조정
        format = 'JPEG',           # 최종 저장 포맷
        options = {'quality': 60}  # 저장 옵션
    ) 
    name = models.CharField(max_length=10)    # 상품이름
    description = models.TextField()    # 상품정보
    
        # 삭제함수는 수정중에 있습니다 --> 오류 발견 10/26 김영환    
    def delete(self, *args, **kargs): 
        os.remove(os.path.join(settings.MEDIA_ROOT+"portfolio/", self.image.path))
        super(Portfolio, self).delete(*args, **kargs) # 원래의 delete 함수를 실행
        
    # 업데이트시 이전사진 삭제 --> 잘 돌아감 10/26 김영환    
    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Portfolio.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Portfolio, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name