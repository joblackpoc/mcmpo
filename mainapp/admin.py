from django.contrib import admin
from .models import Book, Post, Comment
# Register your models here.

admin.site.register(Book)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'created_at')
    search_fields = ('name', 'email', 'body')