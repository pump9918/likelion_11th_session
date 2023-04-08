from django.shortcuts import render

# Create your views here.
def mainpage(reqeust):
    return render(reqeust, 'main/mainpage.html')

def secondpage(request):
    return render(request, 'main/secondpage.html')

def thirdpage(request):
    return render(request, 'main/thirdpage.html')