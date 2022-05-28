from django import forms

#입력등의 폼 이미정의되어있음

class SaleForm(forms.Form):
    first_name=forms.CharField()
    last_name=forms.CharField()
    age=forms.IntegerField(min_value=0)