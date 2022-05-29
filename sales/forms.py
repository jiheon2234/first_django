from django import forms
from .models import Sale
from django.contrib.auth.forms import UserCreationForm,UsernameField
from django.contrib.auth import get_user_model
User = get_user_model()
#입력등의 폼 이미정의되어있음

class SaleModelForm(forms.ModelForm): #필드지정할필요 x
    class Meta: #models에서 만들어놓은 모델 (sale)사용
        model=Sale
        fields= ( #보여줄 필드
            'first_name',
            'last_name',
            'age',
            'person'
        )


class SaleForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    age=forms.IntegerField(min_value=0)


class 우리만의UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =("username",)
        field_classes = {'username' : UsernameField}
