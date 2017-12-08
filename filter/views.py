from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('my_profile')
    else:
        form = UserCreationForm()
    return render(request, 'filter/signup.html', {'form': form})

def my_profile(request):
    myProfile = User.objects.all()
    return render(request, 'filter/my_profile.html')

def profile_list(request):
    users = User.objects.all()
    return render(request, 'filter/profile_list.html', {'users':users})
'''
def update_profile(request, user_id):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('my_profile')
    else:
        form = UserCreationForm()
    return render(request, 'filter/signup.html', {'form': form})
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()
'''
