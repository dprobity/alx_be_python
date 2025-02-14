from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    price = models.DecimalField()
    category = models.CharField()
    