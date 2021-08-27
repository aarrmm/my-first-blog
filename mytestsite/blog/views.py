from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    # posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.all().order_by('title')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# get_object_or_404 : 404오류가 뜰 경우 page not found페이지 출력
