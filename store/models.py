from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=0)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postal_code = models.IntegerField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    stock = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    created = models.DateField()
    updated = models.DateField()


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateField()
    updated = models.DateField()
    CHOICES_PAID = (
        ('Оплачено', "Оплачено"),
        ("Не Оплачено", "Не Оплачено")
    )
    paid = models.CharField(choices=CHOICES_PAID, max_length=100)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField()








