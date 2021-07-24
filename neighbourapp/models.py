from django.db import models
from django.contrib.auth.models import User

# Create your models here.class Post(models.Model):
class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    pub_date = models.DateTimeField()  
    author= models.ForeignKey(User,on_delete = models.CASCADE)  
    votes_total = models.IntegerField(default=1)

    def publication_date(self):
        return self.pub_date.strftime('%b %e, %Y')

class Profile(models.Model):
    name = models.CharField(max_length=255)
    
class Business(models.Model):
    pass

class 