from django import forms
from .models import Sale

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