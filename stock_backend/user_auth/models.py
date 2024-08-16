from django.db import models
## this library will allow me to import a basic model
from django.contrib.auth.models import AbstractUser
from rest_framework import serializers




## Creating this taking it from the deault data that is seen in the AbstractUser template
class CustomUser(AbstractUser):
    pass
    

## Serialiser will allow me to convert data from different datatypes into JSON format
class UserSerializer(serializers.ModelSerializer):
    ## this inludes all of the fields that should be inluded when perfoming the serialisation
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    ## this will make it soo that this will help with creating a new user and adding their data into the database 
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user