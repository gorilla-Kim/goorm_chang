from django.test import TestCase
from django.db import models
from . models import Intro, About, Service, Contact, Portfolio
from . import views
from django.urls import reverse
# Create your tests here.
class test_Mainsite(TestCase):
    @classmethod
    def setUpClass(cls):
        super(test_Mainsite, cls).setUpClass()
        
        intro = Intro(
            client = 'exampleperson'
        )
        intro.save()
        
        service = Service(
            tech_name = 'metal',
            tech_content = 'metalslug'
        )
        service.save()
        
        about = About(
            context = '123123123'
        )
        about.save()
        
        contact = Contact(
            office = 'seoul',
            call = '01071883841',
            pax = '123123',
            email = 'nexus2493@gmail.com'
        )
        contact.save()

        portfolio = Portfolio(
            name  = "imgname",
            description = "imgdes",
            image = "C:/Users/13053/OneDrive/바탕 화면/주석 2019-12-02 193930.jpg",
            
        )
        portfolio.save()
    
class Board_Category_ModelTestCase(test_Mainsite):
    def test_Category(self):
        print('Mainsite App test')
        intro = Intro.objects.get(client = 'exampleperson')
        about = About.objects.get(context = '123123123')
        service = Service.objects.get(tech_name = 'metal')
        contact = Contact.objects.get(office = 'seoul')
        portfolio = Portfolio.objects.get(name = "imgname")
        
        self.assertEqual(intro.client, 'exampleperson')
        self.assertEqual(service.tech_name, 'metal')
        self.assertEqual(service.tech_content, 'metalslug')
        self.assertEqual(about.context, '123123123')
        self.assertEqual(contact.office, 'seoul')
        self.assertEqual(contact.call, '01071883841')
        self.assertEqual(contact.pax, '123123')
        self.assertEqual(contact.email, 'nexus2493@gmail.com')
        self.assertEqual(portfolio.name, 'imgname')
        self.assertEqual(portfolio.description,'imgdes')
        self.assertEqual(portfolio.image,"C:/Users/13053/OneDrive/바탕 화면/주석 2019-12-02 193930.jpg")
        print('Product App test success')
        


#views.py test
class HomePageTests(TestCase):
    print('\n')
    print("Mainsite App view.py test")
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('main'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'mainsite/index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Chang-Won')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
        
    print("Mainsite App view.py test success")
      