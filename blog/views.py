from django.shortcuts import render
from blog.models import Post


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = { 'posts': posts }
    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories_name_contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'blog_category.html', context)