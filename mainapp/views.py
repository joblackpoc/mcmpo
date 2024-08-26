from django.shortcuts import render, redirect
from . models import Book
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
            