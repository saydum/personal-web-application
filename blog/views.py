from django.shortcuts import render
from django.views import generic
from .models import Post

def index(request):
    return render(request, "/home/saydum/core/templates/blog/index.html", {})

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = '/home/saydum/core/templates/blog/posts.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = '/home/saydum/core/templates/blog/post_deatail.html'
