from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    location_lat = models.FloatField()
    location_long = models.FloatField()
    address = models.CharField(max_length=700)

class Deal(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    end_date = models.DateTimeField()
    start_date = models.DateTimeField()
    original_price = models.IntegerField()
    deal_price = models.IntegerField()
    nubmer_of_peoples_bought = models.IntegerField(default=0)
    number_of_peoples_viewed = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)

class PhoneNumber(models.Model):
    number = models.CharField(max_length=13)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)

class ItemImage(models.Model):
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)


