from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('register/', create, name='register'),
    path('', auth_views.LoginView.as_view(template_name='resident/login.html'), name='login'),
]