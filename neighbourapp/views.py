from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import NewPost, RegistrationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.timezone import utc


@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.order_by('-votes_total')
    return render(request, 'index.html', {'posts':posts})

@login_required(login_url='/accounts/login/') 
def profile(request):
    

    posts = Post.objects.order_by('-votes_total')
    return render(request, 'index.html', {'posts':posts})




def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        
        if form.is_valid():        
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
        return redirect('login')
    else:
        form= RegistrationForm()
    return render(request, 'registration/registration_form.html', {"form":form}) 


@login_required
 

def post(request):
  
    current_user = request.user
    if request.method == 'POST':
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            announce = form.save(commit=False)
            announce.user = current_user
            announce.save()
        return redirect('index')
    else:
        form = NewPost()
    return render(request, 'announce.html', {"form": form})    