from django.db import models
from myaccount.models import *
class Tag(models.Model):
    name = models.CharField(max_length=50)


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    
    
# first_name = "moustafa"
# last_name = "shahin"
# email = "moustafashahin@outlook.com"
# password = 123
# user_default = user_reg(first_name=first_name)
# user_default.last_name= last_name
# user_default.email = email
# user_default.password = password
# user_default.save()

class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    target = models.FloatField()
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    average_rate = models.FloatField(default=0)
    owner=models.ForeignKey(user_reg, on_delete=models.CASCADE)

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


# assign average rate to project
def assign_average_rate(project_id):
    project = Project.objects.get(id=project_id)
    rates = Rate.objects.filter(project=project_id)
    total_rate = 0
    for rate in rates:
        total_rate = total_rate + rate.rate
    average_rate = total_rate / len(rates)
    project.average_rate = average_rate
    project.save()
