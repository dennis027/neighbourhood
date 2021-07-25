from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import NewNeighborForm, NewPost, ProfileUpdateForm, RegistrationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.timezone import utc
from .forms import UserUpdateForm,ProfileUpdateForm


@login_required(login_url='/accounts/login/')
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

@login_required(login_url='/accounts/login/') 
def profile(request):
    

    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

@login_required(login_url='/accounts/login/') 
def emergency(request):
    return render(request, 'emergency.html')

@login_required(login_url='/accounts/login/') 
def neighbor(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighborForm(request.POST, request.FILES)
        if form.is_valid():
            neighbor = form.save(commit=False)
            neighbor.user = current_user
            neighbor.save()
        return redirect('index')
    else:
        form = NewNeighborForm()
    return render(request, 'neighbor.html',{'form':form})    


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

@login_required(login_url='/accounts/login/')
# def profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = NewProfile(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.user = current_user
#             user.save()
#         return redirect('profile')
#     else:
#         form = NewProfile()
#     return render(request, 'profile.html',{"form": form})    

@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user)
        u_form = UserUpdateForm(request.POST,instance=request.user)

        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            # messages.success(request,'Your Profile has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user)
        u_form = UserUpdateForm(instance=request.user)

    context={'p_form': p_form, 'u_form': u_form}
    return render(request, 'profile.html',context )

    