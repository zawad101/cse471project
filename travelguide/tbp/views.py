
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import TravelerLoginForm, TravelerRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import TravelerUpdateForm




# Create your views here.


def home(request):
    return render(request,'home.html',{})

def register(request):
    if request.method == 'POST':
        form = TravelerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = TravelerRegistrationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = TravelerLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page.
    else:
        form = TravelerLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home') 

# Import the custom user model
from .models import traveler

def reset_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        try:
            
            user = traveler.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password has been successfully updated.')
            return redirect('home')  
        except traveler.DoesNotExist:
            messages.error(request, 'User does not exist.')
            return redirect('reset_password')  

    return render(request, 'reset_password.html')  

# views.py

def update_profile(request):
    if request.method == 'POST':
        form = TravelerUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_updated')  # Redirect to a success page
    else:
        form = TravelerUpdateForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})

def profile_updated(request):
    return render(request, 'profile_updated.html')


@login_required  # Ensures that only logged-in users can access this view
def view_profile(request):
    # Retrieve the traveler instance associated with the logged-in user
    profile = request.user

    # Pass the profile information to the template
    return render(request, 'profile.html', {'profile': profile})