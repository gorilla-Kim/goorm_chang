from django.db import models
import os
# Create your models here.

# 상품 종류 DB
class KindOfProduct(models.Model):
    name = models.CharField(max_length=100, primary_key=True)    # 상품종류 이름
    
    def __str__(self):
        return self.name
    
# 상품 DB
class Product(models.Model):
    kindOf = models.ForeignKey(KindOfProduct, on_delete=models.CASCADE) # kindofproduct 외래키 참조
    name = models.CharField(max_length=10)    # 상품이름
    description = models.TextField()    # 상품정보
    price = models.IntegerField()    # 가격정보
    photo = models.ImageField(upload_to="products")    # 상품 사진이름
    
    created_at = models.DateTimeField(auto_now_add=True)    # 해당 레코드 생성시 현재 시간 자동저장
    updated_at = models.DateTimeField(auto_now=True)    # 해당 레코드 갱신시 현재 시간 자동저장
    
    def __str__(self):
        return self.name
    
    # 삭제함수는 수정중에 있습니다 --> 오류 발견 10/26 김영환    
    def delete(self, *args, **kargs): 
        os.remove(os.path.join(settings.MEDIA_ROOT+"products/", self.photo.path))
        super(Product, self).delete(*args, **kargs) # 원래의 delete 함수를 실행
        
    # 업데이트시 이전사진 삭제 --> 잘 돌아감 10/26 김영환    
    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Product.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Product, self).save(*args, **kwargs)

class Order(models.Model):
    email = models.EmailField()
    pwd = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    order_count = models.IntegerField()
    description = models.TextField() # 문의 내용
    created_at = models.DateTimeField(auto_now_add=True)    # 해당 레코드 생성시 현재 시간 자동저장

    def __str__(self):
        return self.email

