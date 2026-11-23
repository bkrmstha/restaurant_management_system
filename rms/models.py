from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Table(models.Model):
    name = models.CharField(max_length=3)
    is_available = models.BooleanField(default=True)
    reservation = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"Table no.{self.name}"

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    stock = models.IntegerField()
    minimum_stock = models.IntegerField()

    def __str__(self):
        return f"{self.name}- {self.stock}"

class Order(models.Model):
    status_CHOICES = [
        ("P", "Pending"),
        ("C", "Cancelled"),
        ("CP", "Completed"),
        ("D", "Delivered"),
    ]
    payment_choices = [
        ("P", "Pending"),
        ("PD", "Paid"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    total_price = models.DecimalField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=status_CHOICES,default='P')
    payment_status = models.CharField(max_length=2, choices=payment_choices, default='P')

class Order_Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.menu.name} x {self.quantity}"
    def get_total(self):
        return self.quantity *self.price

class Review(models.Model):

    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

    menu = models.ForeignKey( Menu, on_delete=models.CASCADE, related_name='reviews')

    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.menu.name} ({self.rating}/5)"