from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.crypto import get_random_string

# Create your models here.


class user_reg(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    egy_phone_number = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=16)
    profile_pic = models.ImageField(upload_to='photos/')
    birth_date = models.DateField(null=True)
    fb_profile = models.CharField(null=True)
    activated = models.BooleanField(null=True)
    activation_key = models.CharField(max_length=40, blank=True)
