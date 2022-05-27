2022-5-26시작!!!!
Python 3.9.7 (django_practice)
django-admin startproject [이름] 
python manage.py runserver  //서버실행
python manage.py migrate  //기능들 적용 (db)
python mange.py startapp [앱이름] // 앱 만들기
python manage.py makemigrations // (sales)라는 DB만들어짐 id는 자동생성됨
python manage.py migrate // DB에 반영이 됨 (db.sqlite3)

python manage.py createsuperuser //슈퍼유저(admin)만들기

//확인
python mange.py shell
from django.contrib.auth import get_user_model
아이디=get_user_model()
아이디.objects.all()
from sales.models import Person
관리자 = 아이디.objects.get(username="admin")
//Person에 관리자 등록
회원 = Person.objects.create(회원=관리자)

Sale에 관리직원 등록
관리직원 = Person.objects.get(회원__email="admin@admin.com")
Sale.objects.create(first_name="길동",last_name="홍",age=200,person=관리직원)

템플릿폴더만들기(templates) 아니면 sales밑 templates가 default
setting.py의 TEMPLATES의 dir 안에 폴더 넣기