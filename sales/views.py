from operator import ge
from django.shortcuts import render,redirect,reverse   #render=랜더링생각
from django.http import HttpResponse
from .models import Sale,Person
from .forms import SaleForm,SaleModelForm
from django.views import generic #장고 기본제공으로 한번에 만들기

# Create your views here.

class 첫화면View(generic.TemplateView):
    template_name: "첫화면.html"
################################
def 첫화면(request):
    return render(request, "첫화면.html") 


class 세일목록View(generic.ListView):
    template_name = "folder/세일목록.html"
    queryset= Sale.objects.all()
    context_object_name =  '사람키' #컨텍스트 집어넣기

##########################
def 세일목록(request):
    사람 = Sale.objects.all()
    context = {
        "사람키":사람
    }
    return render(request, "folder/세일목록.html", context) #context=html을 동적으로만드는 dict()
    #기본적으로 templates밑으로 바꿀러면 settings.py설정

class 세일상세View(generic.DetailView):
    template_name="folder/세일상세.html"
    queryset = Sale.objects.all()
    context_object_name = "사람키"
#############################
def 세일상세(request,pk): #urls.py에서받았던 pk를 받음
    # print(pk)
    사람 = Sale.objects.get(id=pk)
    # print(세일)
    
    context={
        "사람키":사람
    }
    return render(request,"folder/세일상세.html",context)

class 세일_입력View(generic.CreateView):
    template_name = "folder/세일_입력.html"
    form_class = SaleModelForm
    def get_success_url(self) :
        return reverse("홈페이지:목록") #redirect


def 세일_입력(request):
    폼=SaleModelForm()
    if request.method=='POST':
        폼 = SaleModelForm(request.POST)
        if 폼.is_valid(): #유효하면
            폼.save() #db에 저장

            return redirect("/홈페이지")

    context={
        "폼키": 폼,
    }

    return render(request,"folder/세일_입력.html",context)

class 세일_업데이트View(generic.UpdateView):
    template_name = "folder/세일_업데이트.html"
    queryset = Sale.objects.all()
    form_class = SaleModelForm
    context_object_name = "사람키"
    def get_success_url(self) -> str:
        return reverse("홈페이지:목록")

############################
def 세일_업데이트(request,pk):
    사람 = Sale.objects.get(id=pk)

    폼=SaleModelForm(instance=사람)
    if request.method=='POST':

        폼=SaleModelForm(request.POST,instance=사람)
        if 폼.is_valid():
            폼.save()
            return redirect("/홈페이지")
    context={
        "폼키":폼,
        "사람키" : 사람
        }
    
    return render(request,"folder/세일_업데이트.html",context)

class 세일_지우기View(generic.DeleteView):
    template_name = "folder/세일_지우기.html"
    queryset = Sale.objects.all()
    def get_success_url(self) :
        return reverse("홈페이지:목록")
###############################
def 세일_지우기(request,pk):
    사람=Sale.objects.get(id=pk)
    사람.delete()
    return redirect("/홈페이지")

""" def 세일_업데이트(request,pk):
    사람 = Sale.objects.get(id=pk)

    폼=SaleForm()
    if request.method=='POST':
        폼 = SaleForm(request.POST)
        if 폼.is_valid(): #유효성 체크
            first_name=폼.cleaned_data["first_name"]
            last_name=폼.cleaned_data["last_name"]
            age=폼.cleaned_data["age"]
            person=Person.objects.first()

            사람.first_name = first_name
            사람.last_name = last_name
            사람.age=age
            사람.save()

            return redirect("/홈페이지")
    context={
        "폼키":폼,
        "사람키" : 사람
        }
    
    return render(request,"folder/세일_업데이트.html",context) """
    
""" def 세일_입력(request):
    폼=SaleForm()
    if request.method=='POST':
        print("포스트 메소드로 왔네요")
        폼 = SaleForm(request.POST)
        if 폼.is_valid(): #유효성 체크
            print("유효")
            print(폼.cleaned_data)
            first_name=폼.cleaned_data["first_name"]
            last_name=폼.cleaned_data["last_name"]
            age=폼.cleaned_data["age"]
            person=Person.objects.first()

            Sale.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                person=person
            )

            print("세일이 입력 되었습니다")
            return redirect("/홈페이지")

    context={
        "폼키": 폼,
    }

    return render(request,"folder/세일_입력.html",context) """
