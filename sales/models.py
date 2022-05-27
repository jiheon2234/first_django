from django.db import models

# Create your models here. (DB)

class Sale(models.Model):
    경로_선택 = (
        ('nr','네이버'),
        ('shop2','샵투원드'),
        ('news','이메일뉴스레터')
    )
    first_name = models.CharField(max_length=30) 
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)

    기존고객 = models.BooleanField(default=False)
    유입경로 = models.CharField(choices=경로_선택,max_length=200)
    인물사진 = models.ImageField(blank=True,null=True) #사진
    파일 = models.FileField(blank=True,null=True) #blank=빈채로저장허용 null=db null