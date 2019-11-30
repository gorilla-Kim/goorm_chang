from django.shortcuts import render,redirect
from .models import Board_Category, Board
# 페이지네이션, - 2019-11-09 김영환 추가
from django.core.paginator import Paginator

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


# Create your views here.
def main(request):
    context ={}
    board_category = None;
    boards = None;
    
    # category 가져오기
    kind = request.GET.get('kind')
    try:
        # 만약에 kind 데이터가 없다면...
        if kind==None or kind=="공지사항":
            # 제일 첫번째 kind 객체를 사용한다.
            kind = "공지사항" 
            board_category = Board_Category.objects.get(name = kind)
            boards = Board.objects.filter(board_category = board_category)
        else:
            board_category = Board_Category.objects.get(name = kind)
            boards = Board.objects.filter(board_category = board_category)

        # == 페이지네이션 관련 소스 시작 -김영환 ==
        # Show 3 contacts per page
        paginator = Paginator(boards, 7) 
        page = request.GET.get('page')
        contacts = paginator.get_page(page)
        # == 페이지 네이션 관련 소스 끝 ==
        
        print("="*10+"test!!"+"="*10)
    except:
        print("="*10+" mainpage 관련 DB 오류 "+"="*10)
    
    
    context = {
        # 에러를 제거하기 위한 사용 김영환
        "error":error_handeler(request, False, ""), 
        "title":"Chang-Won", 
        "boards": boards, 
        "category": Board_Category.objects.all(),
        # 현재 경로를 식별하기 위한 값 09.11.09 김영환
        "path": request.path,  
        "contacts": contacts,
        "kind": kind
    }
    return render(request, 'board/index.html', context)



def create_board(request):
    context = {}
    if request.method == 'POST':
        board_category = request.POST.get("board_category")
        subject = request.POST.get("subject")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        content = request.POST.get("content")
        admin_option = True if request.POST.get("admin_option")=="on" else False
        
        board = Board( 
            board_category = Board_Category.objects.get(name=board_category),
            subject = subject,
            email = email,
            pwd = pwd,
            content = content,
            admin_option = admin_option
        )
        
        board.save()
        return redirect("board_main")
        
    else:
        context = {
            # 에러를 제거하기 위한 사용 김영환
            "error":error_handeler(request, False, ""), 
            "title":"Chang-Won", 
            # category 모두 가져오기
            "category": Board_Category.objects.all(),
            # 현재 경로를 식별하기 위한 값 09.11.09 김영환
            "path": request.path,  
        }
        print("test")
        return render(request, 'board/board.html', context)

# 일단 보류
def update_board(request):
    return render(request, 'board/index.html', context)

# 일단 보류
def delete_board(request):
    return render(request, 'board/index.html', context)

def read_board(request, pk):
    context = {
            # 에러를 제거하기 위한 사용 김영환
            "error":error_handeler(request, False, ""), 
            "title":"Chang-Won", 
            # category 모두 가져오기
            "category": Board_Category.objects.all(),
            # 현재 경로를 식별하기 위한 값 09.11.09 김영환
            "path": request.path, 
    }
    board = Board.objects.get(id = pk)
    if(board.admin_option):
        error_handeler(request, True, "관리자만 확인 가능합니다.")
        return redirect("board_main")
        
    print("="*30)
    print(board)
    context["board"] = board
    return render(request, 'board/boardView.html', context)
    