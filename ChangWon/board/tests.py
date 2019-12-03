from django.test import TestCase
from django.db import models
from . models import Board, Board_Category
from django.urls import reverse
from django.shortcuts import redirect
# Create your tests here.
class test_Board_Category(TestCase):
    @classmethod
    def setUpClass(cls):
        super(test_Board_Category, cls).setUpClass()
        board = Board_Category(
            name="공지사항",                  
            admin_option = False,                   
            created_at=1,                 
            updated_at=1
        )
        board.save()
        
        boards = Board(
  
            board_category = Board_Category.objects.get(name = '공지사항'),
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
        ob = Board_Category.objects.get(name = '공지사항')
        self.assertEqual(ob.name, '공지사항')
        self.assertEqual(ob.admin_option, False)
        self.assertEqual(str(ob.created_at)[:10], '2019-12-03')
        self.assertEqual(str(ob.updated_at)[:10], '2019-12-03')
        obs = Board.objects.get(subject= 'testsubject')
        self.assertEqual(obs.subject, 'testsubject')
        self.assertEqual(obs.email, 'test@gmail.com')
        self.assertEqual(obs.content, 'test')
        self.assertEqual(obs.hit, 1)
        self.assertEqual(obs.admin_option, True)
        self.assertEqual(obs.ifmodify,"n")
        print('Board App test success')


# views.py test
class HomePageTests(TestCase):
    print('\n')
    print("Board App view.py test")

    def test_view_uses_correct_template1(self):
        board = Board_Category(
            name="공지사항",                  
            admin_option = False,                   
            created_at=1,                 
            updated_at=1
        )
        board.save()
        response = self.client.get('/board/')
        self.assertEquals(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'board/index.html')



    def test_view_uses_correct_template2(self):
        self.client.login(username='user', password='test')
        response = self.client.get('/board/read/18')
        
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(redirect('main'))

    def test_view_uses_correct_template2(self):
        self.client.login(username='user', password='test')
        response = self.client.get('/board/update_board/18')
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(redirect('board_main'))
        
    def test_view_uses_correct_template2(self):
        boards = Board_Category(
            name="공지사항",                  
            admin_option = False,                   
            created_at=1,                 
            updated_at=1
        )
        boards.save()
        ob = Board.objects.create(board_category = Board_Category.objects.get(name = '공지사항'),
            subject = 'testsubject',
            email = 'test@gmail.com',
            content = 'test',
            hit = 1,
            admin_option = True,
            created_at = 1,
            updated_at = 1,
            ifmodify = "n")
        ob.save()
        print(ob)
        self.client.login(username='user', password='test')
        response = self.client.get('/board/updatepage/%d' %ob.id)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'board/update.html')
def test_view_uses_correct_template2(self):
    boards = Board_Category(
        name="공지사항",                  
        admin_option = False,                   
        created_at=1,                 
        updated_at=1
    )
    boards.save()
    ob = Board.objects.create(board_category = Board_Category.objects.get(name = '공지사항'),
        subject = 'testsubject',
        email = 'test@gmail.com',
        content = 'test',
        hit = 1,
        admin_option = True,
        created_at = 1,
        updated_at = 1,
        ifmodify = "n")
    ob.save()
    print(ob)
    self.client.login(username='user', password='test')
    response = self.client.get('/board/delete_board/%d' %ob.id)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(redirect('board_main'))

        
        


    print("Board App view.py test success")
      