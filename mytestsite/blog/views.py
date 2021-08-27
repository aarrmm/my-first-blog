# get_object_or_404 : 404오류가 뜰 경우 page not found페이지 출력
from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User

def post_list(request):
    # posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.all().order_by('title')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)           # 글 쓰고 데이터를 넘겨줄떄
        if form.is_valid():
            post = form.save(commit=False)      # 작성자추가 후 저장하려고 False로...
            post.author = request.user  # 그냥 하면
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()   # 처음 접속했을 때(글쓰기)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk): # pk를 매개변수로 받아서 ㄱ
    post = get_object_or_404(Post, pk=pk) # 수정하려는 글의 Post모델인스턴스를 가져옴
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
