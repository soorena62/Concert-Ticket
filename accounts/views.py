from accounts.forms import ProfileEditForm, ProfileRegisterForm, UserEditForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tickets.views import concertlistview
from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from .models import Profile
import accounts
import tickets
# Create your views here:


def loginview(request):
    #Post
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get("next"))
                
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context={
                "username":username,
                "errorMessage":"کاربری با این مشخصات یافت نشد"
            }
            return render(request, "accounts/login.html",context)
     #Get
    else:
        return render(request, "accounts/login.html",{})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse(tickets.views.concertlistview))


@login_required
def profileview(request):
    profile = request.user.profile

    context = {
        "profile":profile
    }
    return render(request, 'accounts/profile.html', context)


def profile_register_view(request):
    if request.method=="POST":
        profileRegisterForm=ProfileRegisterForm(request.POST,request.FILES)
        if profileRegisterForm.is_valid():

            user = User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                                email=profileRegisterForm.cleaned_data['email'],
                                password=profileRegisterForm.cleaned_data['password'],
                                first_name=profileRegisterForm.cleaned_data['first_name'],
                                last_name=profileRegisterForm.cleaned_data['last_name'])

            user.save()

            profile=Profile(user=user,
                                       profile_image=profileRegisterForm.cleaned_data['profile_image'],
                                        gender=profileRegisterForm.cleaned_data['gender'],
                                        credit=profileRegisterForm.cleaned_data['credit'])

            profile.save()

            return HttpResponseRedirect(reverse(tickets.views.concertlistview))
    else:
        profileRegisterForm=ProfileRegisterForm()

  
    context={
        "formData":profileRegisterForm
    }

    return render(request, "accounts/Register-profile.html", context)


def profile_edit_view(request):
    
    if request.method=="POST":
        profileEditForm=ProfileEditForm(request.POST,request.FILES, instance=request.user.profile)
        userEditForm=UserEditForm(request.POST,instance=request.user)
        if profileEditForm.is_valid and userEditForm.is_valid:
            profileEditForm.save()
            userEditForm.save()
            return HttpResponseRedirect(reverse(accounts.views.profileview))
    else:
        profileEditForm=ProfileEditForm(instance=request.user.profile)
        userEditForm=UserEditForm(instance=request.user)

    context={

        "profileEditForm":profileEditForm,
        "userEditForm":userEditForm,
        "ProfileImage":request.user.profile.ProfileImage,
        
    }

    return render(request,"accounts/edit-profile.html",context)