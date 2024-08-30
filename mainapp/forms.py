from django import forms
from .models import Book, Comment, Post
from django_ckeditor_5.fields import CKEditor5Field

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        content = CKEditor5Field(config_name='default')
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']