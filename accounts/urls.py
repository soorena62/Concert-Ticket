from django.contrib import admin
from django.urls import path
from accounts import views



urlpatterns = [
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview),
]