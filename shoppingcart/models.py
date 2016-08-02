from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone

class PersonalInfo(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(null=True, blank=True )
    address = models.CharField(max_length=50)
    phone = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract=True

class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True )
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(PersonalInfo,TimeStamp):
    cart = models.TextField(null=True)

class Vendor(PersonalInfo,TimeStamp):
    description = models.CharField(max_length=50)

class Category(TimeStamp):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    parent = models.ForeignKey('self')


class Product(TimeStamp):
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    feature = models.TextField()
    vendor = models.ForeignKey(Vendor)
    tags = models.TextField()
    category = models.ForeignKey(Category)


class Order(TimeStamp):
    customer = models.ForeignKey(Customer)


class OrderItem(TimeStamp):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    price = models.IntegerField()

