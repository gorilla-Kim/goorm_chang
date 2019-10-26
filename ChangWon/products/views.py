from django.shortcuts import render

# Create your views here.
# product들의 리스트를 보여주는 페이지입니다 - 김영환
def main(request):
    context = {"error":True, "title":"Chang-Won"}
    return render(request, 'products/index.html', context)