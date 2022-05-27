from django.urls import path
from .views import 세일목록,세일상세

app_name = "홈페이지"
urlpatterns=[   ##철자주의
    path('',세일목록),
    path('<pk>/',세일상세), #<>안의 정보를 받음
   

]