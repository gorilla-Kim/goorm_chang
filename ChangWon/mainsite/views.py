from django.shortcuts import render
from .models import About
from .models import Intro
from .models import Service
from .models import Contact
from .models import Contact

# Create your views here.
def main(request):
    try:
        client = Intro.objects.all()
        about = About.objects.all()
        tech =  Service.objects.all()
        contact = Contact.objects.all()
    except:
        print("="*10+" mainpage 관련 DB 오류 "+"="*10)
    context = { 
        "title":"Chang-Won",
        "client":client,
        "about":about,"tech":tech, 
        "contact":contact, 
        "path": request.path  # 현재 경로를 식별하기 위한 값 09.11.09 김영환
    }
    return render(request, 'mainsite/index.html', context)