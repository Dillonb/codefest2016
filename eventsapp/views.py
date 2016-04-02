from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from eventsapp.models import *
from eventsapp.forms import *

# Create your views here.

def home_view(request):
    if request.user.is_authenticated():
        return render(request,"eventsapp/home.html")
    else:
        return redirect("/accounts/login")

@login_required
def profile_view(request):
    user = request.user

    return render(request, "eventsapp/profile.html", {"user": user})

@login_required
def account_view(request):
    return render(request, "eventsapp/account.html")

def logout_view(request):
    pass

@login_required
def calendar_view(request):
	return render(request, "eventsapp/calendar.html")

def day_view(request):
	return render(request, "eventsapp/day.html")

def week_view(request):
	return render(request, "eventsapp/week.html")

def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def calendar_list_view(request):
    return render(request, "eventsapp/list.html", {
        "events": Event.objects.all()
    })

@login_required
def submit_event_view(request):
    form = EventForm(data=request.POST)

    if form.is_valid():
        e = Event()
        e.description = form.cleaned_data['description']
        e.name = form.cleaned_data['name']
        e.user = request.user
        e.save()
        return redirect("/calendar/list")
    return render(request, "eventsapp/submit.html", {"form": form})
