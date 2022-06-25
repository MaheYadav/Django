from django.db import models

class Producce(models.Model):
    p_no=models.IntegerField(primary_key=True)
    p_name=models.CharField(max_length=30)
    p_price=models.DecimalField(max_digits=10,decimal_places=2)
    p_image=models.ImageField(upload_to='media/')