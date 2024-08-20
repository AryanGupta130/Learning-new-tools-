from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, RegisterForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages


## the generics.CreateAPIView is a buitl in class that handles creating new model instances in a database
## this is used to handle the post request for adfding a new user on the dayabase with all the users
class RegisterView(generics.CreateAPIView):
    ## this is a list of all the queries that are being performed on the CustomUser model
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    ## anyone can access the registration page without thier being logged in
    permission_classes = [AllowAny]
    
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Automatically log in the user after registration
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Registration successful! Welcome to the site.')
                return redirect('home')  # Redirect to a home page or any other page after registration
            else:
                messages.error(request, 'There was an issue logging you in. Please try logging in manually.')
                return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'user_auth/registration/register.html', {'form': form})  # Update the path here

def home(request):
    return render(request, 'user_auth/registration/home.html')
