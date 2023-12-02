from django.shortcuts import render
from tickets.models import Concert, Location
# Create your views here:


def concertlistview(request):
    concerts = Concert.objects.all()
    context = {
        "concertlist":concerts,
        "concertcount":concerts.count()
    }
        
    return render(request, "tickets/concertlist.html", context)

def locationlistview(request):
    locations = Location.objects.all()
    context = {
        "locationlist":locations,
    }
        
    return render(request, "tickets/locationlist.html", context)


def concert_detailsview(request, concert_id):
    concert = Concert.objects.get(pk=concert_id)
    context = {
        "concertdetails":concert
    }
    return render(request, "tickets/concertdetail.html", context)

