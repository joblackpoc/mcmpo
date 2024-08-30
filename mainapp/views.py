from django.shortcuts import render, redirect, get_object_or_404
from . models import Book, Post, Comment
from . forms import BookForm

# Create your views here.
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            publication_date = form.cleaned_data['publication_date']
            Book.objects.create(title=title, author=author, publication_date=publication_date)
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'mainapp/book_form.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'mainapp/book_list.html', {'books': books})

def update_book(request, pk):
    books = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=books)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=books)
    return render(request, 'mainapp/book_form.html', {'form':form})

def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'mainapp/confirm_delete.html', {'book': book})
            

from .forms import CommentForm

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })