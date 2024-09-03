from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from . models import Post
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'post' : post})
    

    