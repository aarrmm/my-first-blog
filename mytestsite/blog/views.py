from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    # posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    posts = Post.objects.all().order_by('title')
    return render(request, 'blog/post_list.html', {'posts': posts})
