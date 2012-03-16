from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Menu(models.Model):
    vendor_location_id = models.CharField(max_length=256)
    categories = models.ManyToManyField('Category', null=True, blank=True)
    
class Category(models.Model):
    name = models.CharField(max_length=256)
    items = models.ManyToManyField('Item', null=True, blank=True)
    
class Item(models.Model):
    item_id = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    
    