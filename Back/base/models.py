from django.db import models

# Create your models here.
class Product(models.Model):
   Desc = models.CharField(max_length=100)
   Price = models.IntegerField()

   def __str__(self):
       return self.Desc