#Migration is creating tables in database using models
from django.db import models

# Create your models here.

class Destinations(models.Model):
    
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    desc=models.TextField()
    price=models.IntegerField(default=0)
    offer=models.BooleanField(default=False)
