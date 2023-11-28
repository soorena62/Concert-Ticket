from django.contrib import admin

from .models import Concert, Ticket, Time, Profile, Location

# Register your models here:


admin.site.register(Concert)
admin.site.register(Ticket)
admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(Time)

