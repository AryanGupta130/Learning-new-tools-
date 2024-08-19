from django.urls import path
from .views import RegisterView

urlpatterns = [
    # URL pattern for the registration endpoint
    path('register/', RegisterView.as_view(), name='register'),
    
   
]
