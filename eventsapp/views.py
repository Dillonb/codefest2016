from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from eventsapp.models import *
from eventsapp.forms import *
import datetime

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

def calendar_view(request):
	return render(request, "eventsapp/calendar.html")

def day_view(request):
	return render(request, "eventsapp/day.html")

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
        e.save()
        return redirect("/calendar/list")
    return render(request, "eventsapp/submit.html", {"form": EventForm()})
