from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    supplier_name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=100,blank=True)
    email=models.EmailField(blank=True)
    address=models.TextField(blank=True)

    def __str__(self):
        return self.name
