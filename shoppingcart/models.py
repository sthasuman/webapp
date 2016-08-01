from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dateofbirth =models.DateTimeField()
    address = models.CharField()
    phone = models.IntegerField()
    email = models.CharField()

class Vendor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.IntegerField(max_length=5)