from django.shortcuts import render
from django.urls import reverse
import accounts
import tickets
from tickets.models import Concert, Location, Time
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from tickets.forms import ConcertForm, SearchForm
# Create your views here:


def concertlistview(request):
    searchform = SearchForm(request.GET)
    if searchform.is_valid():
        Searchtext=searchform.cleaned_data["Searchtext"]
        concerts = Concert.objects.filter(name__contains=Searchtext)
    else:
        concerts = Concert.objects.all()  

    context = {
        "concertlist":concerts,
        "concertcount":concerts.count(),
        "searchform":searchform,
    }
        
    return render(request, "tickets/concertlist.html", context)


@login_required
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


@login_required
def timeview(request):

    # if request.user.is_authenticated  and request.user.is_active:

        times=Time.objects.all()
        
        context={

            "timelist":times,
        }

        return render(request, "tickets/timelist.html", context)

    # else:
    #     return HttpResponseRedirect(reverse(accounts.views.loginView))


def concert_edit_view(request, concert_id):
    concert=Concert.objects.get(pk=concert_id)
    if request.method == 'POST':
        concertform = ConcertForm(request.POST, request.FILES, instance=concert)
        if concertform.is_valid:
            concertform.save()
            return HttpResponseRedirect(reverse(tickets.views.concertlistview))
    else:
        concertform = ConcertForm(instance=concert)

    context={

            "concertform":concertform,
            "PosterImage":concert.poster
        }
    return render(request,"tickets/editconcert.html",context)
