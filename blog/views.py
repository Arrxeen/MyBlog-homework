from django.shortcuts import render
from blog import models

def post(request):
    posts = models.Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request,'blog/post_list.html', context)

def author_post(request, pk):
    author = models.Author.objects.get(id=pk)
    context ={
        'author_posts': author.posts.all()
    }

    return render(request, 'blog/author_posts.html', context)

def post_detail(request, pk):
    post = models.Post.objects.get(id=pk)
    context = {
        "post": post,
        'published_recently': post.published_recently()
    }

    return render(request,'blog/post_detail.html', context)