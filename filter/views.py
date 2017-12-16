from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm, ProfileForm
from django.contrib import messages
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
            return redirect('render_home')
    else:
        form = UserCreationForm()
    return render(request, 'filter/signup.html', {'form': form})

@login_required
def my_profile(request):
    myProfile = User.objects.all()
    return render(request, 'filter/myprofile.html')

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('myprofile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'filter/updateprofile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def search(request):
    users = User.objects.all()
    return render(request, 'filter/search.html', {'users': users})

@login_required
def profile_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'filter/profile_detail.html', {'user': user})

@login_required
def render_home(request):
    myProfile = User.objects.all()
    return render(request, 'filter/home.html')
