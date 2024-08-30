from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"