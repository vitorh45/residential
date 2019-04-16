from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('login/', auth_views.LoginView.as_view(template_name='resident/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', detail, name='detail'),
]