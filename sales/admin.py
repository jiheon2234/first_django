from django.contrib import admin
from .models import 아이디,Sale,Person,UserProfile
admin.site.register(아이디) #어드민사이트에 등록 (각각해야됨)
admin.site.register(Sale)
admin.site.register(Person)
admin.site.register(UserProfile)


# Register your models here.

