
from django.shortcuts import render, redirect # redirect 추가 - 2019 10 27 남승철 추가
from django.core.mail import EmailMessage # 메일 객체 생성시 필요함 - 2019-10-26 남승철 추가
from .models import Product, Request # 순서대로 문의, 발주 DB - 2019-10-28 박은혜 추가
 
# Create your views here.

# error message handler function -김영환
def error_handeler(request, msg):
    err_msg = ""
    if request.session.get('error', False):
        err_msg = request.session['error']
        del request.session['error']
    else:
        request.session['error'] = msg
    return err_msg

# product들의 리스트를 보여주는 페이지입니다 - 김영환
def main(request):
    
       
    # products = Product.objects.all() --> 심세은님 부탁드립니다. 
    context = {"error":error_handeler(request, msg), "title":"Chang-Won"}
    
    return render(request, 'products/index.html', context)


# 2019-10-26 남승철 추가 
# !문제! :  발신자 메일을 지정할 방법이 아직 없음;;;  찾아보는 중...

def sendEmail(request):                     # 문의 사항 이메일 보내기 및 db에 등록
    who = request.POST.get("email")         # 문의자 이름 or id
    content = request.POST.get("content")   # 문의 내용
    
    # 메일 보내기
    emailcontent = EmailMessage()                      # 이메일 객체 생성
    emailcontent.subject = "문의사항"
    emailcontent.body =  content                       # 내용
    emailcontent.from_email = 'flash0211@naver.com'    # 발신지
    emailcontent.to = ['flash0211@naver.com']          # 목적지
    emailcontent.send() 

    # 문의사항 db에 저장 - 2019-10.28 박은혜 추가
    try :
        Request(email = who, content = content).save()
    except:
       request(email = None, content = None).save()

    return redirect('main')


def order(request):
    email = request.POST.get("email")
    pw = request.POST.get("pw")
    subject = request.POST.get("subject")
    desc = request.POST.get("description")
    count = request.POST.get("count")

    # 메일 보내기
    emailcontent = EmailMessage()                            # 이메일 객체 생성
    emailcontent.subject = subject
    emailcontent.body =  count                              # 내용
    emailcontent.from_email = 'flash0211@naver.com'         # 발신지
    emailcontent.to = ['flash0211@naver.com']               # 목적지
    emailcontent.send() 

    # 주문 내용을 디비에 저장  - 2019-10.28 박은혜 추가, 2019-11-03 김영환 수정
    try:
        Request(
            email = email, 
            pw = pw,
            subject = subject, 
            description = desc,
            order_count = count, 
        ).save()
    except:
        error_handeler(request, "- DB 오류 -")

    return redirect('main')