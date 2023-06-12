from django.db import models
from myaccount.models import *
class Tag(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    target = models.FloatField()
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    owner=models.ForeignKey(user_reg, on_delete=models.CASCADE,default=1)

class Photo(models.Model):
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.FileField(upload_to='photos/')
    # image = models.FileField()

class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    comment = models.TextField()
    
class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    amount = models.FloatField()

class Report(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    report = models.BooleanField(default=False)

class Rate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(user_reg, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)