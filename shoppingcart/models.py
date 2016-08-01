from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateTimeField()
    address = models.CharField()
    phone = models.IntegerField()
    email = models.CharField()

class Customer(models.Model):
    personal_info = models.ForeignKey(PersonalInfo)
    cart = models.CharField()

class Vendor(models.Model):
    personal_info = models.ForeignKey(PersonalInfo)
    description = models.CharField(max_length=50)

class Product(models.Model):
    prod_name = models.CharField()
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField()
    stock = models.IntegerField(max_length=20)
    feature = models.TextField()
    vendor = models.ForeignKey(Vendor)
    tags = models.TextField()
    category = models.CharField()

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

class Order(models.Model):
    customer = models.ForeignKey(Customer)
    time = models.DateTimeField()