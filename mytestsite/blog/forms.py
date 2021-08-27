from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        # exclude = ()

# class Meta
# -> 이 폼을 만들기 위해 어떤 model이 쓰여야 하는지 알려주는 구문
# 여기서는 Post를 사용하겠다는 의미.
# 이 폼에 필드를 넣으면 완성
# author는 로그인한 사용자, created_date는 글 등록시간이라 작성X
