from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from . models import Post
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'