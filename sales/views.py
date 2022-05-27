from django.shortcuts import render     #render=랜더링생각
from django.http import HttpResponse
from .models import 아이디
# Create your views here.

def 홈페이지(request):
    드실분 = 아이디.objects.all()
    context = {
        "메뉴명" : "짜장",
        "가격" : "700원",
        "손님" : 드실분,
    }
    return render(request, "아무거나2.html", context) #context=html을 동적으로만드는 dict()
    #기본적으로 templates밑으로 바꿀러면 settings.py설정