from django.urls import path
from .views import 세일목록,세일상세,세일_입력,세일_업데이트,세일_지우기,세일_입력View,세일목록View,세일상세View,세일_업데이트View,세일_지우기View

app_name = "홈페이지1111"
urlpatterns=[   ##철자주의
    path('',세일목록View.as_view(),name='목록'),
    path('<int:pk>/',세일상세View.as_view(),name="상세"), #<>안의 정보를 받음 #int안해주면 밑에도 숫자로입력해서문제생김
    path('ma_monde/',세일_입력View.as_view(),name='생성'),
    path('<int:pk>/업데이트/',세일_업데이트View.as_view(),name='업뎃'),
    path('<int:pk>/지우기/',세일_지우기View.as_view(),name='지우기'),
]

# <!--{% url namespace:name %}--> 
# ==namespace 에서 name을 찾아서 연결!!