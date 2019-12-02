from django.test import TestCase
from django.db import models
from . models import Board, Board_Category
from django.urls import reverse

# Create your tests here.
class test_Board_Category(TestCase):
    @classmethod
    def setUpClass(cls):
        super(test_Board_Category, cls).setUpClass()
        board = Board_Category(
            name="testname",                  
            admin_option = False,                   
            created_at=1,                 
            updated_at=1
        )
        board.save()
        
        boards = Board(
            board_category = Board_Category.objects.get(name = 'testname'),
            subject = 'testsubject',
            email = 'test@gmail.com',
            content = 'test',
            hit = 1,
            admin_option = True,
            created_at = 1,
            updated_at = 1,
            ifmodify = "n"
        )
        
        boards.save()
    
    
class Board_Category_ModelTestCase(test_Board_Category):
    def test_Category(self):
        print('Board App test')
        ob = Board_Category.objects.get(name = 'testname')
        self.assertEqual(ob.name, 'testname')
        self.assertEqual(ob.admin_option, False)
        self.assertEqual(str(ob.created_at)[:10], '2019-12-02')
        self.assertEqual(str(ob.updated_at)[:10], '2019-12-02')
        obs = Board.objects.get(subject= 'testsubject')
        self.assertEqual(obs.subject, 'testsubject')
        self.assertEqual(obs.email, 'test@gmail.com')
        self.assertEqual(obs.content, 'test')
        self.assertEqual(obs.hit, 1)
        self.assertEqual(obs.admin_option, True)
        self.assertEqual(obs.ifmodify,"n")
        print('Product App test success')


#views.py test
class HomePageTests(TestCase):
    print('\n')
    print("Board App view.py test")
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('board_main'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'Chang-Won')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
        
    ###########################################################
    
    def test_home_page_status_code2(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


    def test_view_uses_correct_template2(self):
        response = self.client.get(reverse('read/13'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/index.html')

    def test_home_page_contains_correct_html2(self):
        response = self.client.get('/')
        self.assertContains(response, 'Chang-Won')

    def test_home_page_does_not_contain_incorrect_html2(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
        
    print("Board App view.py test success")
      