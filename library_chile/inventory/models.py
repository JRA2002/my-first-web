from django.db import models
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    Supplier = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
   
