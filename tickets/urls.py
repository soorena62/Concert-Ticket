from django.contrib import admin
from django.urls import path
from tickets import views

from tickets.views import concert_detailsview, concertlistview,\
                        concert_edit_view,locationlistview, timeview



urlpatterns = [
    path('admin/', admin.site.urls),
    path('concert/list/', views.concertlistview),
    path('location/list/', views.locationlistview),
    path('concert/<int:concert_id>', views.concert_detailsview),
    path('time/list/', views.timeview),
    path('concertedit/<int:concert_id>', views.concert_edit_view),
    
]