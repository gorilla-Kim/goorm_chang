from django.test import TestCase, Client

# Create your tests here.
from django.core.mail import EmailMessage # 메일 객체 생성시 필요함 - 2019-10-26 남승철 추가 

class CustomTests(TestCase):
    def order():
        check = False
          
        try:
            emailcontent = EmailMessage()                           # 이메일 객체 생성
            emailcontent.subject = subject
            emailcontent.body =  count                              # 내용
            emailcontent.from_email = 'flash0211@naver.com'         # 발신지
            emailcontent.to = ['flash0211@naver.com']               # 목적지
            emailcontent.send()
            check = True
        except:
            check = False
        self.assertTrue(check)
        
class post(TestCase):
    
    c = Client()
    response = c.get('/products/order')
    print(response.status_code)
    response = c.post('/products/order', {'email': 'nexus2493@gmail.com', 'subject': '제목', 'order_count': 1, 'description': "sdfdf"})
    print(response.status_code)
    