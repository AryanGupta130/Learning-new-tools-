'''
from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

## the generics.CreateAPIView is a buitl in class that handles creating new model instances in a database
## this is used to handle the post request for adfding a new user on the dayabase with all the users
class RegisterView(generics.CreateAPIView):
    ## this is a list of all the queries that are being performed on the CustomUser model
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    ## anyone can access the registration page without thier being logged in
    permission_classes = [AllowAny]
    '''
    
from django.http import HttpResponse
from django.urls import path

def test_view(request):
    return HttpResponse("Test view is working")

urlpatterns = [
    path('test/', test_view, name='test'),
]
