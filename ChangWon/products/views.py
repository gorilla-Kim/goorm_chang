from django.shortcuts import render, redirect # redirect 추가 - 2019 10 27 남승철 추가
from django.core.mail import EmailMessage # 메일 객체 생성시 필요함 - 2019-10-26 남승철 추가
from .models import Product, Order, KindOfProduct # 순서대로 문의, 발주 DB - 2019-10-28 박은혜 추가
from django.core.paginator import Paginator # 페이지네이션, - 2019-11-09 김영환 추가
  
# ========================================
#             에러 핸들러 사용법 -김영환
#-----------------------------------------
# parameter (아래 참고) 
# request : request, 
# activate : 실행모드(True=error생성, False=에러출력 및 삭제), 
# msg : message
#=========================================
# error message handler function -김영환
def error_handeler(request, active, msg):
    err_msg = ""
    if request.session.get('error', False) and not active:
        err_msg = request.session['error']
        del request.session['error']
    elif active == True:
        request.session['error'] = msg
    return err_msg

# product들의 리스트를 보여주는 페이지입니다 - 김영환
def main(request):
    kinds = KindOfProduct.objects.all()
    products = Product.objects.filter(kindOf = 1)
    # == 페이지네이션 관련 소스 시작 -김영환 ==
    paginator = Paginator(products, 3) # Show 3 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    
    # == 페이지 네이션 관련 소스 끝 ==
    context = {
        "error":error_handeler(request, False, ""), # 에러를 제거하기 위한 사용 김영환
        "title":"Chang-Won", 
        "products": products, 
        "kinds": kinds,
        "path": request.path,   # 현재 경로를 식별하기 위한 값 09.11.09 김영환
        "contacts": contacts
    }
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
        Request(email = None, content = None).save()

    return redirect('main')


def order(request):
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    desc = request.POST.get("description")
    count = request.POST.get("count")

    # 메일 보내기
    emailcontent = EmailMessage()                            # 이메일 객체 생성
    emailcontent.subject = subject
    emailcontent.body =  count                           # 내용
    emailcontent.from_email = 'flash0211@naver.com'         # 발신지
    emailcontent.to = ['flash0211@naver.com']               # 목적지
    emailcontent.send() 

    # 주문 내용을 디비에 저장  - 2019-10.28 박은혜 추가, 2019-11-03 김영환 수정
   
    try:
        Order(
            email = email, 
            subject = subject, 
            order_count =int(count), 
            description = desc ).save()
    except:
        error_handeler(request, True, "- DB 오류 -")

    return redirect('productsList')