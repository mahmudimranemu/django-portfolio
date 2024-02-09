from django.shortcuts import render
from . models import Post, Category

def index(request):
    posts = Post.objects.all().order_by("-created_at")
    context ={
        "posts":posts
    }
    return render(request, "blog/index.html", context);

def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    context={
        "post":post
    }
    return render(request, "blog/single.html", context)

def category_post(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by("-created_at")
    context={
        "category":category,
        "posts":posts
    }

    return render(request, "blog/category-posts.html", context)