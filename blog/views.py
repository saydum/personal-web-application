from django.shortcuts import render
from django.views import generic
from .models import Post

def index(request):
    return render(request, "blog/index.html", {})

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'blog/posts.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_deatail.html'
