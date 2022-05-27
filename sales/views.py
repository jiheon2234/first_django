from django.shortcuts import render     #render=랜더링생각
from django.http import HttpResponse
from .models import Sale
# Create your views here.

def 세일목록(request):
    사람 = Sale.objects.all()
    context = {
        "사람키":사람
    }
    return render(request, "folder/세일목록.html", context) #context=html을 동적으로만드는 dict()
    #기본적으로 templates밑으로 바꿀러면 settings.py설정

def 세일상세(request,pk): #urls.py에서받았던 pk를 받음
    # print(pk)
    사람 = Sale.objects.get(id=pk)
    # print(세일)
    
    context={
        "사람키":사람
    }
    return render(request,"folder/세일상세.html",context)