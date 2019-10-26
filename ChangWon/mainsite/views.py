from django.shortcuts import render

# Create your views here.
def main(request):
    context = {"error":True, "title":"Chang-Won"}
    return render(request, 'mainsite/index.html', context)