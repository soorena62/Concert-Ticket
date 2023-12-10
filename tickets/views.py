from django.shortcuts import render
from django.urls import reverse
import accounts
from tickets.models import Concert, Location, Time
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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


def timelistview(request):
    times = Time.objects.all()
    context = {
        "timelist":times,
    }
    return render(request, "tickets/timelist.html", context)

@login_required
def timeView(request):

    if request.user.is_authenticated  and request.user.is_active:

        times=Time.objects.all()
        
        context={

            "timelist":times,
        }

        return render(request,"tickets/timelist.html",context)

    else:
        return HttpResponseRedirect(reverse(accounts.views.loginView))
    