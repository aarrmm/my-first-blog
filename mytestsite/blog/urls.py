from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('post/<int:pk>/', views.post_detail, name="post_detail"),
    path('post/new/', views.post_new, name="post_new"),
    path('post/<int:pk>/edit', views.post_edit, name="post_edit"),
]

# post_list라는 view를 url에 할당.
# 'http://127.0.0.1:8000/' 주소로 접속했을 때
# views의 post_list를 보여줌
# name="post_list"은 뷰를 식별하기위해 이름 붙인 것. 뷰와 이름이 다를수도 있음
# <int:pk> : 정수값을 pk라는 변수로 view에 전송
