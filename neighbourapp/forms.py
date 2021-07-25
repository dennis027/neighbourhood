from neighbourapp.models import  Post,User,Profile,NeighbourHood
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields



class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

    def save(self, commit=True):
        user=super().save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user     

class NewPost(forms.ModelForm):
    class Meta:
        model=Post
        exclude = []
        Fields = ['title','user','subject']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        exclude = ['neighborhood_id']
        fields=['username','email']    


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['pic','bio']          


class NewNeighborForm(forms.ModelForm):
    class Meta:
        model= NeighbourHood
        fields=['name','location','occupation_count']        