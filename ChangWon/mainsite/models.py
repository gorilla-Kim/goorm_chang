from django.db import models

# Create your models here.
class Intro(models.Model):
    client = models.CharField(max_length=50)
    def __str__(self):
        return self.client

class About(models.Model):
    context = models.TextField()
    def __str__(self):
        return self.context

class Service(models.Model):
    tech_name = models.CharField(max_length=500)
    tech_content = models.TextField()
    def __str__(self):
        return self.tech_name

class Contact(models.Model):
    office = models.CharField(max_length = 50)
    call = models.CharField(max_length=100)
    pax = models.CharField(max_length=100)
    email =models.EmailField(max_length=254)
    def __str__(self):
        return self.office