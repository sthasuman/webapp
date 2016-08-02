from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    user = models.OneToOneField(User)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateTimeField(null=True, blank=True )
    address = models.CharField(max_length=50)
    phone = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True

class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Customer(models.Model):
    personal_info = models.ForeignKey(PersonalInfo)
    cart = models.TextField()
    time_stamp = models.ForeignKey(TimeStamp)
    status = models.IntegerField(
        (1, 'Verified'),
        (2, 'Not Verified'),
        default= 0
    )

class Vendor(models.Model):
    personal_info = models.ForeignKey(PersonalInfo)
    time_stamp = models.ForeignKey(TimeStamp)
    description = models.CharField(max_length=50)
    status = models.IntegerField(
        (1, 'Verified'),
        (2, 'Not Verified'),
        default= 0
    )

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField(max_length=20)
    discount = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    feature = models.TextField()
    vendor = models.OneToManyField(Vendor)
    tags = models.TextField()
    category = models.OneToManyField(Category)
    time_stamp = models.DateTimeField(TimeStamp)

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    parent = models.ForeignKey('self')
    time_stamp = models.DateTimeField(TimeStamp)

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    time_stamp = models.DateTimeField(TimeStamp)

class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(max_length=20)
    price = models.IntegerField(max_length=20)
    time_stamp = models.DateTimeField(TimeStamp)
