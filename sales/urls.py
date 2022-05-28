from django.urls import path
from .views import 세일목록,세일상세,세일_입력,세일_업데이트,세일_지우기

app_name = "홈페이지"
urlpatterns=[   ##철자주의
    path('',세일목록),
    path('<int:pk>/',세일상세), #<>안의 정보를 받음 #int안해주면 밑에도 숫자로입력해서문제생김
    path('make/',세일_입력),
    path('<int:pk>/업데이트/',세일_업데이트),
    path('<int:pk>/지우기/',세일_지우기)
]