from django.urls import path
from .views import 홈페이지

app_name = "홈페이지"
urlpatterns=[   ##철자주의
    path('',홈페이지)

]