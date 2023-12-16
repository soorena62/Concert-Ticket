from django.contrib import admin
from django.urls import path
from accounts import views



urlpatterns = [
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('profile/', views.profileview, name='profile'),
    path('profileregister/', views.profile_register_view, name='profileregister'),
    path('profileedit/', views.profile_edit_view, name='profileedit'),
    
]