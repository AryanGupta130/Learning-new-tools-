from django.urls import path
from .views import register, home  # HTML view
from .api_views import RegisterView  # API view

urlpatterns = [
    path('register/', register, name='register'),  # HTML registration form
    path('api/register/', RegisterView.as_view(), name='api_register'),  # API registration
    path('', home, name='home'),  
]
