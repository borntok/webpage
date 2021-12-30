from django.urls import path
from django.urls.conf import include
from django.views.generic.base import TemplateView

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signIn/', auth_views.LoginView.as_view(template_name = 'accounts/signin.html')),
    path('signOut/', auth_views.LogoutView.as_view()),
    path('signUp/', views.signup),
    path('createUser/', views.createUser),
    
]