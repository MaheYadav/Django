from django.db import models

class Product(models.Model):
    no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    image=models.ImageField(upload_to="products/")