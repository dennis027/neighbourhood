from django.db import models
from django.contrib.auth.models import User


# Create your models here.class Post(models.Model):


class Post(models.Model):
    title = models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete = models.CASCADE)
    subject = models.CharField(max_length=255,default="")

class NeighbourHood(models.Model):
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=200)
    occupation_count = models.IntegerField(default=0)
    admin = models.ForeignKey
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=255)
    neighborhood_id = models.ForeignKey(NeighbourHood,on_delete= models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Business(models.Model):
    name = models.CharField(max_length=25)
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    neighborhood_id = models.ForeignKey(NeighbourHood,on_delete= models.CASCADE)
    bussiness_email= models.EmailField()    
    def __str__(self):
        return self.name