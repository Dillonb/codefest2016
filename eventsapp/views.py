from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from eventsapp.models import *
from eventsapp.forms import *

from eventsapp.models import *

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
def club_view(request, clubid):
    club = get_object_or_404(Club, id=clubid)
    return render(request, "eventsapp/club.html", {"club":club})

@login_required
def club_list_view(request):
    return render(request, "eventsapp/club_list.html", {"clubs": Club.objects.all()})

@login_required
def club_submit_view(request):
    form = ClubForm(data=request.POST)

    if form.is_valid():
        e = Club()
        e.name = form.cleaned_data['name']
        e.save()
        return redirect("/clubs/list")
    return render(request, "eventsapp/club_submit.html", {"form": form})

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
