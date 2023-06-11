from django.db import models

# Create your models here.
class user_reg(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100 )
    email=models.EmailField(max_length=100 , unique=True)
    phone_num=models.CharField(max_length=11)
    password = models.CharField(max_length=16)
    profile_pic=models.ImageField(upload_to='photos/')
    birth_date=models.DateField(null=True)
    fb_profile=models.CharField(null=True)
    activated = models.BooleanField(null=True)


