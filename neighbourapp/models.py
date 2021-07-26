from django.db import models
from django.contrib.auth.models import User


# Create your models here.class Post(models.Model):

class Profile(models.Model):
    bio=models.TextField()
    pic=models.ImageField(default='default.jpg',upload_to='profile_pics')
    user = models.OneToOneField(User, related_name='profile',on_delete= models.CASCADE)
    def __str__(self):
        return self.bio   
class Post(models.Model):
    title = models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete = models.CASCADE)
    subject = models.CharField(max_length=255,default="")

class NeighbourHood(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=200)
    occupation_count = models.IntegerField(default=0)
    admin = models.ForeignKey
    def __str__(self):
        return self.name

    
    def save_neighbour(self):
        self.save()

    def delete_neighbour(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        neighborhood = cls.objects.get(id = neighborhood_id)
        return neighborhood

    @classmethod
    def update_neighborhood(cls, neighborhood_id):
        neighborhood  = cls.objects.filter(id=neighborhood_id).update()
        return neighborhood

    @classmethod
    def update_count(cls, count):
        neighborhood_count = cls.objects.filter(occupants_count=1).update(occupants_count=count)
        return neighborhood_count
    

class User(models.Model):
    name = models.CharField(max_length=255)
    neighborhood_id = models.ForeignKey(NeighbourHood,on_delete= models.CASCADE)
    email = models.EmailField()
    user_image = models.ImageField(upload_to='images/',default='woman.png')

    def __str__(self):
        return self.name


      

class Business(models.Model):
    name = models.CharField(max_length=25)
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    neighborhood_id = models.ForeignKey(NeighbourHood,on_delete= models.CASCADE)
    bussiness_email= models.EmailField()    
    def __str__(self):
        return self.name


    def __str__(self):
        return self.business_name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, search_term):
        return cls.objects.filter(business_name__icontains=search_term).all()    


    