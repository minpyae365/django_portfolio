from django.db import models

# Create your models here.

class Intro(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    short_description = models.TextField(max_length=150)
    about = models.TextField(null=True,blank=True)
    categories = models.ManyToManyField('Category', related_name='skills')

    def __str__(self):
        return self.name


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


class Contact(models.Model):
    name = models.CharField(max_length=30)
    icon_name = models.CharField(max_length=15, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name