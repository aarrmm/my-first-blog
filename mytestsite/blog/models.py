from django.db import models
from django.conf import settings
from django.utils import timezone


# 모델(객체) 정의 코드
# models는 Post가 장고모델임을 의미하여 DB에 저장하는 것을 인식
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# models.CharField(글자수) : 글자수가 제한된 text를 정의할 때 사용.
#                            글제목처럼 짧은 문자열 정보저장
# models.TextField() : 글자수에 제한이 없는 긴 text를 정의
#                      글 내용에 적합
# models.DateTimeField() : 날짜와 시간을 의미
# models.ForeignKey() : 다른 모델에 대한 링크를 의미
# 공식문서 참조 https://docs.djangoproject.com/en/3.2/ref/models/fields/ 

# 생성된 데이터를 DB에 반영(makemigrations)
