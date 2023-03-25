from django.db import models
from django.utils import timezone
from django.contrib import admin


class Listing(models.Model):

    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name.__str__() + "'s Item"