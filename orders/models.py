from django.db import models
from django.conf import settings
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None
=======
    status = models.CharField(max_length=10, default='Pending')
>>>>>>> 9750d19510afba2425c8776ebd6db6b453cef295

    def __str__(self):
        return f'Order {self.id} by {self.user.username}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
<<<<<<< HEAD

    def __str__(self):
        return f'{self.quantity} of {self.product.name}'
=======
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} for Order {self.order.id}"
>>>>>>> 9750d19510afba2425c8776ebd6db6b453cef295
