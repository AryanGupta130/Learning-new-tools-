from django.urls import path
from .views import register, home, login_view
from .api_views import RegisterView  # API view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),  # HTML registration form
    path('api/register/', RegisterView.as_view(), name='api_register'),  # API registration
    path('login/', login_view, name='login'),  # Login view
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', home, name='home'),  # Home view
]

