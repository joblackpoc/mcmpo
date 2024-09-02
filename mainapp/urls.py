from django.urls import path
from .views import HomeView, ArticleDetailView, IndexDetailView, IndexView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('index/', IndexView.as_view(), name='index'),
    path('detail/<int:pk>', IndexDetailView.as_view(), name='detail'),
]
