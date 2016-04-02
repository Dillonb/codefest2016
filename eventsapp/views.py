from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    if request.user.is_authenticated():
        return redirect("/calendar")
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
