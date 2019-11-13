from django.shortcuts import render, redirect # redirect 추가 - 2019 10 27 남승철 추가
from django.core.mail import EmailMessage # 메일 객체 생성시 필요함 - 2019-10-26 남승철 추가
from .models import Product, Order, KindOfProduct # 순서대로 문의, 발주 DB - 2019-10-28 박은혜 추가
from django.core.paginator import Paginator # 페이지네이션, - 2019-11-09 김영환 추가
from django.http import JsonResponse # json답변을 위한 라이브러리, - 2019-11-10 김영환 추가
  
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
    kind = request.GET.get('kind')
    if kind==None: # 만약에 kind 데이터가 없다면...
        kind = KindOfProduct.objects.first() # 제일 첫번째 kind 객체를 사용한다.
        
    products = Product.objects.filter(kindOf = kind)
    
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
        "contacts": contacts,
        "kind": kind
    }
    return render(request, 'products/index.html', context)


def order(request):
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    desc = request.POST.get("description")
    count = request.POST.get("count")
    file = request.FILES["addfile"] # pdf 받아오기 2019 11.13 남승철 추가
    # 메일 보내기
    emailcontent = EmailMessage()                            # 이메일 객체 생성
    emailcontent.subject = subject
    emailcontent.body =  count 
    emailcontent.attach("주문양식.pdf",file.read(),'application/pdf') # 파일첨부 2019 11.13 남승철 추가
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

def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    kinds = KindOfProduct.objects.all()
    context = {
        'product':product,
        'kinds': kinds,
        "path": request.path,  # 현재 경로를 식별하기 위한 값 09.11.09 김영환
    }
    return render(request, 'products/product.html', context)
