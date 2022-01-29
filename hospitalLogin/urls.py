from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signUp', views.signUp, name='signUp'),
    path('signUpRedirect', views.signUpRedirect, name='signUpRedirect'),
    path('login', view=views.login, name='login')
]