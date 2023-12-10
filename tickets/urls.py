from django.contrib import admin
from django.urls import path
from tickets import views

from tickets.views import concert_detailsview, concertlistview,\
                        locationlistview, timelistview



urlpatterns = [
    path('admin/', admin.site.urls),
    path('concert/list/', views.concertlistview),
    path('location/list/', views.locationlistview),
    path('concert/<int:concert_id>', views.concert_detailsview),
    path('time/list/', views.timelistview),
    
]