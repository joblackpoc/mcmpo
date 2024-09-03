from django.urls import path
from .views import HomeView, ArticleDetailView
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('index', views.index, name='index'),
    path('<int:pk>', views.detail, name='detail'),
]
