from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
# 요청을 받아서 render라는 메소드를 호출하고 post_list.html을 보여줌

