from django.contrib import admin
from .models import Intro
from .models import About
from .models import Service
from .models import Contact
from .models import Portfolio

# Register your models here.
admin.site.register(Intro)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Portfolio)