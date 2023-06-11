from django.db import models

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


class Photo(models.Model):
    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.FileField(upload_to='photos/')
    # image = models.FileField()

