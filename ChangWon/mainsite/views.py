from django.shortcuts import render
from .models import About
from .models import Intro
from .models import Service
from .models import Contact
from .models import Contact

# Create your views here.
def main(request):
    client = Intro.objects.all()
    about = About.objects.get(id = 1)
    tech =  Service.objects.all()
    contact = Contact.objects.all()
    context = {"error":True, "title":"Chang-Won","client":client,"about":about,"tech":tech, "contact":contact}
    return render(request, 'mainsite/index.html', context)