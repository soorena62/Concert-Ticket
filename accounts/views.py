from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

import tickets
# Create your views here:


def loginview(request):
    # POST:
    if request.method == "post":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        
        else:
            context={
                'username':username,
                'ErrorMessage':"کاربری با این مشخصات یافت نشد"
            }
            return render(request, 'accounts/login.html',context)
    else:
        #GET        
        return render(request, 'accounts/login.html', {})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse(tickets.views.concertlistview))