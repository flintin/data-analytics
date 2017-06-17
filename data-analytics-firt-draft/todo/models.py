from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ToDo(models.Model):

    title = models.CharField(max_length=140, unique=True)
    content = models.TextField(max_length=250)
    createdate = models.DateTimeField(auto_now_add=True)
    tododate = models.DateTimeField()
    user = models.ForeignKey("auth.User")
    done = models.BooleanField(default=False)
    publish = models.BooleanField(default=True)


    def __unicode__(self):
        return self.title

    class Meta:

        ordering = ["-createdate"]
#*********************************************************
class Author(models.Model):
    name = models.CharField(max_length=140, unique=True)
    email = models.EmailField(max_length=254, unique = True)
    age = models.IntegerField()

    def __unicode__(self):
        return self.title

    # class Meta:

    #     ordering = ["-createdate"]    

class Book(models.Model):
    bookname = models.CharField(max_length=140, unique=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    Author = models.CharField(max_length=140, unique=True)
    Publisher = models.CharField(max_length=140, unique=True)
    publish = models.DateField()
    #picname = models.CharField(max_length=140, unique=True)
    pic = models.ImageField(upload_to='media/')
    #user = models.ForeignKey("auth.User")  
    #imageurl = models.ImageField(upload_to="media")
    def __unicode__(self):
        return self.bookname

    # class Meta:

    #     ordering = ["-createdate"]

class Publisher(models.Model):
    pubname = models.CharField(max_length=140, unique=True)
    numawards = models.IntegerField()
    def __unicode__(self):
        return self.title

    # class Meta:

    #     ordering = ["-createdate"]

class Store(models.Model):
    storename = models.CharField(max_length=140, unique=True)
    address = models.TextField(max_length=250)
    booksnum = models.IntegerField()
    registeredusers = models.IntegerField()
    def __unicode__(self):
        return self.title

    # class Meta:

    #     ordering = ["-createdate"]
