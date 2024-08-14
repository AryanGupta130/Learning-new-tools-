from django.db import models
## this library will allow me to import a basic model
from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework import serializers



# Create your models here.

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=50, default='player')  # e.g., 'player', 'admin'

    def __str__(self):
        return self.username
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type=validated_data.get('user_type', 'player')
        )
        return user