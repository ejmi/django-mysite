from django.shortcuts import render

from django.views import generic
from .models import Post

class ListView(generic.ListView):
    model = Post
    template_name = 'blog/blog.html'

    def get_queryset(self):
        return Post.objects.all().order_by("-date")[:25]

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
