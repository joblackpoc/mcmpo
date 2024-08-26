from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('new/', views.create_book, name='create_book'),
    path('<int:pk>/edit/', views.update_book, name='update_book'),
    path('<int:pk>/delete/', views.delete_book, name='delete_book'),
]
