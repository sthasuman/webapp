from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.http import HttpResponseRedirect, HttpResponse

# Create your models here.

class PersonalInfo(models.Model):

    user = models.OneToOneField(User)

    first_name = models.CharField ()
    last_name = models.CharField()
    dob = models.DateField()
    address = models.CharField()
    phone = models.CharField()

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True

class Customer(models.Model):
    personal_info = models.ForeignKey(PersonalInfo)
    cart = models.CharField()

class Vendor(models.Model):
    personal_info = models.ForeignKey(PersonalInfo)
    description = models.CharField(max_length=50)

class Product(models.Model):
    prod_name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.IntegerField(max_length=20)
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
