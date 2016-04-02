from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from eventsapp.models import *
from eventsapp.forms import *
import datetime
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
        club = Club()
        club.name = form.cleaned_data['name']
        club.creator = request.user
        club.save()
        return redirect("/clubs/list")
    return render(request, "eventsapp/club_submit.html", {"form": form})

def logout_view(request):
    pass

def calendar_view(request):
    return render(request, "eventsapp/calendar.html")

def day_view(request):
	# Find todays date
	today = datetime.datetime.now().date()

	events_today = Event.objects.filter(date_time__day = today.day,
                                        date_time__month = today.month,
                                        date_time__year = today.year)

	return render(request, "eventsapp/day.html", {"events_today":events_today})

def week_view(request):
    today = datetime.datetime.now().date()
    dates = [today + datetime.timedelta(days=i) for i in range(0 - today.weekday(), 7 - today.weekday())]
    days = []

    for day in dates:
        days.append({
            'day': day,
            'events': Event.objects.filter(date_time__year=day.year,
                                              date_time__month=day.month,
                                              date_time__day=day.day).order_by("date_time")
        })

    return render(request, "eventsapp/week.html", {"days": days})

def logout_view(request):
    logout(request)
    return redirect("/")

def calendar_list_view(request):
    return render(request, "eventsapp/list.html", {
        "events": Event.objects.all().order_by("date_time")
    })

@login_required
def submit_event_view(request):
    form = EventForm(data=request.POST)

    if form.is_valid():
        e = Event()
        e.description = form.cleaned_data['description']
        e.name = form.cleaned_data['name']
        e.user = request.user
        e.date_time = form.cleaned_data['date']
        e.user_type = 'U'
        e.save()
        return redirect("/calendar/list")
    return render(request, "eventsapp/submit.html", {"form": EventForm()})


def tests_view(request):
	# Insert events in two different dates to test day_view
	# Event that should show up for day/week view
	e = Event()
	e.description = "This should show up for today"
	e.name = "This should show up for today"
	e.user = request.user
	e.date_time = datetime.datetime.now()
	e.save()

	# Event that should not show up for day view
	e1 = Event()
	e1.description = "This should not show up for today"
	e1.name = "This should not show up for today"
	e1.user = request.user
	e1.date_time = datetime.datetime.now() + datetime.timedelta(days=1)
	e1.save()

	# Event that should not show up for this week
	e2 = Event()
	e2.description = "This should not show up for this week"
	e2.name = "This should not show up for this week"
	e2.user = request.user
	e2.date_time = datetime.datetime.now() + datetime.timedelta(days=20)
	e2.save()

	return redirect("/")
