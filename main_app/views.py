from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

# context = {
#     'books': Book.objects.all(),
#     'categories': Category.objects.all(),
#     'book_form': BookForm(),
#     'cat_form': CategoryForm(),
#     'available_books': Book.objects.filter(status='Available').count(),
#     'sold_books': Book.objects.filter(status='Sold').count(),
#     'rented_books': Book.objects.filter(status='Rented').count(),
# } TODO


def add_cat(request):
    add_category = CategoryForm(request.POST)
    if add_category.is_valid() and 'save-cat' in request.POST:
        add_category.save()


def index(request):
    if request.method == 'POST':
        add_cat(request)
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid() and 'add-book' in request.POST:
            add_book.save()
    context = {
        'books': Book.objects.all(),
        'categories': Category.objects.all(),
        'book_form': BookForm(),
        'cat_form': CategoryForm(),
        'available_books': Book.objects.filter(status='Available').count(),
        'sold_books': Book.objects.filter(status='Sold').count(),
        'rented_books': Book.objects.filter(status='Rented').count(),
    }
    return render(request, 'pages/index.html', context)


def books(request):
    search = Book.objects.all()
    if 'search_name' in request.GET:
        search = search.filter(title__icontains=request.GET['search_name'])
    if request.method == 'POST':
        add_cat(request)

    context = {
        'books': search,
        'categories': Category.objects.all(),
        'cat_form': CategoryForm(),
    }
    return render(request, 'pages/books.html', context)


def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        add_cat(request)
        book_update = BookForm(request.POST, request.FILES, instance=book_id)
        if book_update.is_valid() and 'update-book' in request.POST:
            book_update.save()
            return redirect('/')
    else:
        book_update = BookForm(instance=book_id)

    context = {
        'update_form': book_update,
        'categories': Category.objects.all(),
        'cat_form': CategoryForm(),
    }
    return render(request, 'pages/update.html', context)


def delete(request, id):
    book_id = get_object_or_404(Book, id=id)  # or book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        add_cat(request)
        if 'del-book' in request.POST:
            book_id.delete()
        return redirect('/')
    context = {
        'categories': Category.objects.all(),
        'cat_form': CategoryForm(),
    }
    return render(request, 'pages/delete.html', context)
