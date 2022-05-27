from django.shortcuts import render     #render=랜더링생각
from django.http import HttpResponse

# Create your views here.

def 홈페이지(request):

    return render(request, "아무거나2.html") #기본적으로 templates밑으로 바꿀러면 settings.py설정