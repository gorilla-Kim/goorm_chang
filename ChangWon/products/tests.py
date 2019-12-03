from django.test import TestCase
from django.db import models
from . models import KindOfProduct, Product, Order
from django.urls import reverse

# Create your tests here.
class test_Product(TestCase):
    @classmethod
    def setUpClass(cls):
        super(test_Product, cls).setUpClass()
        
        kindofproduct = KindOfProduct(
            name = "kind"
        )
        kindofproduct.save()
        
        product = Product(
            kindOf = KindOfProduct.objects.get(name = 'kind'),
            name = "1",
            description = "1",
            price = 1,
            photo = "C:/Users/13053/OneDrive/바탕 화면/주석 2019-12-02 193930.jpg",
        )
        product.save()
        
        order = Order(
            email = "1@naver.com",
            pwd = "1",
            subject = "1",
            order_count = 1,
            description = "1"
        )
        order.save()
    
class Board_Category_ModelTestCase(test_Product):
    def test_Category(self):
        print('Product App test')
        kindofproduct = KindOfProduct.objects.get(name = 'kind')
        product = Product.objects.get(name = '1')
        order = Order.objects.get(email = '1@naver.com')
        
        self.assertEqual(kindofproduct.name, 'kind')
        
        self.assertEqual(str(product.kindOf), 'kind')
        self.assertEqual(product.name, '1')
        self.assertEqual(product.description, '1')
        self.assertEqual(product.price, 1)
        self.assertEqual(product.photo, "C:/Users/13053/OneDrive/바탕 화면/주석 2019-12-02 193930.jpg",)
        
        self.assertEqual(order.email, '1@naver.com')
        self.assertEqual(order.pwd, '1')
        self.assertEqual(order.subject, '1')
        self.assertEqual(order.order_count, 1)
        self.assertEqual(order.description, '1')
        print('Product App test success')
        
        
        
#views.py test
class HomePageTests(TestCase):
    print('\n')
    print("Product App view.py test")
    def test_home_page_status_code(self):
        response = self.client.get('/products/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template2(self):
        kindofproduct = KindOfProduct(
            name = "kind"
        )
        kindofproduct.save()
        
        product = Product(
            kindOf = KindOfProduct.objects.get(name = 'kind'),
            name = "1",
            description = "1",
            price = 1,
            photo = "C:/Users/13053/OneDrive/바탕 화면/주석 2019-12-02 193930.jpg",
        )
        product.save()
        
        order = Order(
            email = "1@naver.com",
            pwd = "1",
            subject = "1",
            order_count = 1,
            description = "1"
        )
        order.save()
        
        self.client.login(username='user', password='test')
        response = self.client.get('/products/%d' %product.id)
        self.assertEquals(response.status_code, 301)
        self.assertTemplateUsed('products/product.html')

        
    print("Product App view.py test success")
      
        
      