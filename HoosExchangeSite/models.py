from django.db import models
from django.utils import timezone
from django.contrib import admin
from PIL import Image
import random



class Listing(models.Model):
    TYPES = (
        ("Bottoms", "Bottoms"),
        ("Top", "Top"),
        ("Shoes", "Shoes"),
        ("Accessory", "Accessory"),
    )


    person_name = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100, choices=TYPES)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', default="/HoosExchangeSite/images/noImage.png")
    #img = models.ImageField(upload_to='images/') <-----
    #image = models.ImageField(upload_to='images/') #, default='static/HoosExchangeSite/images/noImage.png'

    def __str__(self):
        return self.person_name.__str__() + "'s Item"

class newModel(models.Model):
    name = models.CharField(max_length=100)