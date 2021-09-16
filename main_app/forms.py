from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'book_image': forms.FileInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'author_avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'pages_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_day_price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rental_price'}),
            'rental_period_by_day': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rental_period'}),
            'total_rental_price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'total_rental_price'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
