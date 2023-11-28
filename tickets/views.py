from django.http import HttpResponse
from django.shortcuts import render
from tickets.models import Concert
# Create your views here:


def concertlistview(request):
    concerts = Concert.objects.all()
    context = {
        "concertlist":concerts,
        "concertcount":concerts.count()
    }
        
    
    return render(request, "tickets/concertlist.html", context)
