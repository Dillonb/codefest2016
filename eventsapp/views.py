from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

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

def logout_view(request):
    pass

#@login_required
def calendar_view(request):
	return render(request, "eventsapp/calendar.html")

def logout_view(request):
    logout(request)
    return redirect("/")
