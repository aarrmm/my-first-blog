from django.contrib import admin
from .models import Post

# 만든 모델(Post)을 보기위해 모델 등록
admin.site.register(Post)

# 웹 서버 실행 후 http://127.0.0.1:8000/admin/로 접속
# 위에서 로그인하려면 admin 계정을 생성해야함(superuser)

# superuser 생성할때는
# cmd창에 python manage.py createsuperuser 를 입력후
# 차례대로 유저명, 아이디, 비밀번호 두번 입력하게됨
# 비밀번호는 화면에 안뜸.

# superuser 삭제할때는
# cmd에서 python manage.py shell 입력하고 shell 오픈
# from django.contrib.auth.models import User
# User.objects.get(username="설정한ID", is_superuser=True).delete()
# 입력하고 잘 지워지면 exit()로 빠져나와서 
# superuser 재생성~

# 저 페이지는 장고에서 기본적으로 제공해주는 관리자페이지 입니다.
# 관리자권한의 사용자가 웹서버의 콘텐츠들을 관리하기위한 도구들을 지원해주는 페이지예요




'''
4. Django의 모델

장고의 모델은 객체로 만든다.

이 객체를 저장하면 그 내용이 DB에 저장됩니다.


ex) 블로그 만들기

블로그라는 객체는 제목, 내용, 글쓴이, 작성일 등을 속성으로 가짐.


(1) app 만들고 settings에 등록하기

- manage.py 가 있는 디렉토리에서 작업

- 어플리케이션 생성


python manage.py startapp blog
내용을 입력하세요.
- Django에 사용을 알리기! (settings.py의 INSTALLED_APPS 수정)


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig'
]
내용을 입력하세요.
blog/apps.py에 정의되어있는 BlogConfig클래스를 등록해 줌


(2) blog 모델 만들기

- blog/models.py에 선언하여 모델을 정의


from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_legnth=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    
    def __str__(self):
        return self.title
'''