"""djangocrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from sales.views import 첫화면,첫화면View
from django.contrib.auth.views import LoginView,LogoutView

LoginView.template_name='회원가입/로그인.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',첫화면View.as_view()),
    path('홈페이지/', include('sales.urls', namespace="홈페이지")), 
    ##namespace = 링크가 바뀔 때 한번에 자동적으로 바뀔 수 있게하는장치!!!! 
    path('로그인/',LoginView.as_view(),name='로긴'),
    path('로그아웃/',LogoutView.as_view(), name='록아웃'),
]
