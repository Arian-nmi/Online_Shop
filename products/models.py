from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    show_in_menu = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
<<<<<<< HEAD
    stock_quantity = models.PositiveIntegerField()  # موجودی مقدار
=======
    stock_quantity = models.PositiveIntegerField()
>>>>>>> 9750d19510afba2425c8776ebd6db6b453cef295
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

