from django.shortcuts import render

# Create your views here.
# product들의 리스트를 보여주는 페이지입니다 - 김영환
def main(request):
    # products = Product.objects.all() --> 심세은님 부탁드립니다. 
    context = {"error":True, "title":"Chang-Won"}
    return render(request, 'products/index.html', context)