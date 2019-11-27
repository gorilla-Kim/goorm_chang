# redirect 추가 - 2019 10 27 남승철 추가
from django.shortcuts import render, redirect 
# 메일 객체 생성시 필요함 - 2019-10-26 남승철 추가
from django.core.mail import EmailMessage 
# 순서대로 문의, 발주 DB - 2019-10-28 박은혜 추가
from .models import Product, Order, KindOfProduct
# 페이지네이션, - 2019-11-09 김영환 추가
from django.core.paginator import Paginator
# json답변을 위한 라이브러리, - 2019-11-10 김영환 추가
from django.http import JsonResponse 
  
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
    # 만약에 kind 데이터가 없다면...
    if kind==None or kind=="all":
        # 제일 첫번째 kind 객체를 사용한다.
        kind = "all" 
        products = Product.objects.all()
    else:
        products = Product.objects.filter(kindOf = kind)
    
    
    # == 페이지네이션 관련 소스 시작 -김영환 ==
    # Show 3 contacts per page
    paginator = Paginator(products, 3) 
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    # == 페이지 네이션 관련 소스 끝 ==
    
    context = {
        # 에러를 제거하기 위한 사용 김영환
        "error":error_handeler(request, False, ""), 
        "title":"Chang-Won", 
        "products": products, 
        "kinds": kinds,
        # 현재 경로를 식별하기 위한 값 09.11.09 김영환
        "path": request.path,  
        "contacts": contacts,
        "kind": kind
    }
    return render(request, 'products/index.html', context)


# 주문서 작성
def order(request):
    desc = ""
    subject= ""
    hiddentag = request.POST.get("order_kind")
    pwd = request.POST.get("pwd")
    email = request.POST.get("email")
    count = request.POST.get("count")
    isFile = request.POST.get("isFile")
    # pdf 받아오기 2019 11.13 남승철 추가
    if isFile == "1":
        file = request.FILES["addfile"]
    question = request.POST.get("content")
    order_kind = request.POST.get("order_kind")
    
    if hiddentag == "1":
        subject = "기성품 주문서" 
        desc = request.POST.get("order_details")
    else:
        subject = "개인 주문서"
        desc = hiddentag

    # 메일 보내기
    # 이메일 객체 생성
    emailcontent = EmailMessage()                           
    emailcontent.body =  email + '\n' + "제품: " + desc +'\n'+ count
    emailcontent.subject = "주문요청" 
    # 파일첨부 기능 pdf 만 됨. 2019 11.13 남승철 추가
    if isFile == "1":
        emailcontent.attach("주문양식.pdf",file.read(),'application/pdf') 
    # 발신지
    emailcontent.from_email = 'nexus2493@gmail.com'
    # 목적지
    emailcontent.to = ['flash0211@naver.com']            
    emailcontent.send() 
    
    # 주문 내용을 디비에 저장  - 2019-10.28 박은혜 추가, 2019-11-03 김영환 수정
    try:
        Order(
            email = str(email),
            pwd = str(pwd),
            subject = str(subject),
            order_count =int(count), 
            description = desc
        ).save()
        
    except:
        error_handeler(request, True, "- DB 오류 -")

    return redirect('productsList')


# 제품을 표시
def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    kinds = KindOfProduct.objects.all()
    context = {
        'product':product,
        'kinds': kinds,
        # 현재 경로를 식별하기 위한 값 09.11.09 김영환
        "path": request.path,  
    }
    return render(request, 'products/product.html', context)
