from django.contrib import admin
from .models import Intro
from .models import About
from .models import Service
from .models import Contact
from .models import Portfolio

# Register your models here.

# 2019.11.20 김영환 수정 
admin.site.site_header = '관리자 페이지입니다.' # 관리자 페이지 Header입니다.

admin.site.register(Intro)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Portfolio)