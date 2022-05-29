from signal import signal
from django.db import models
from django.contrib.auth.models import AbstractUser #이미있는 모델 가져오기 (회원관리)
from django.db.models.signals import post_save
# Create your models here. (DB)

class 아이디(AbstractUser): #상속 
    pass

class UserProfile(models.Model):
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE) #1대1

    def __str__(self) -> str:
        return self.회원.username

class Sale(models.Model):

    def __str__(self) -> str:  #클래스 자체를 출력할때 나오는거
        return self.last_name+self.first_name
    
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("Person", on_delete=models.CASCADE) #외래키
    #지워졌을경우
    #(CASCADE=같이지워짐)  (SET_NULL=null로 바꿈 null=True) (SET_DEFALT DEFALT로 바꿈 defalt='')

    # 기존고객 = models.BooleanField(default=False)
    # 인물사진 = models.ImageField(blank=True,null=True) #사진
    # 파일 = models.FileField(blank=True,null=True) #blank=빈채로저장허용 null=db null


class Person(models.Model):
    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE) #1대1
    조직 = models.OneToOneField(UserProfile,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.회원.username

    #python manage.py migrate

def 회원생성signal(sender, instance, created, **kwargs): # 회원이 만들어지면 Userprofile자동으로 생성
    if created:
        UserProfile.objects.create(회원=instance)

post_save.connect(회원생성signal,sender=아이디) 
#회원이 생성되면, 만들어진 아이디 보내서 자동으로 추가


    