from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=150)
    body = models.TextField(null=True,blank=True)
    categories = models.ManyToManyField('Category', related_name='projects')
    source = models.CharField(max_length=200, null=True, blank=True)
    demo = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.title