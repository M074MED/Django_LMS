from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    status_choices = [('Available', 'Available'), ('Sold', 'Sold'), ('Rented', 'Rented')]
    title = models.CharField(max_length=100)
    book_image = models.ImageField(upload_to='images/books/%y/%m/%d', blank=True, null=True)
    author = models.CharField(max_length=50, blank=True, null=True)
    author_avatar = models.ImageField(upload_to='images/authors/%y/%m/%d', blank=True, null=True)
    pages_num = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rental_day_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rental_period_by_day = models.IntegerField(blank=True, null=True)
    total_rental_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, choices=status_choices, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.title
