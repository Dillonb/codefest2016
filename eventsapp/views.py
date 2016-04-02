from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from eventsapp.models import *
from eventsapp.forms import *
from datetime import datetime
from datetime import timedelta
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

def club_view(request, clubid):
    club = get_object_or_404(Club, id=clubid)
    print(club.event_set.all())
    return render(request, "eventsapp/club.html", {"club":club, "events": club.event_set.all()})

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
    today = datetime.now().date()

    events = Event.objects.filter(date_time__day = today.day,
                                        date_time__month = today.month,
                                        date_time__year = today.year)

    return render(request, "eventsapp/event_list.html", {"days": [{'day':"Today", 'events':events}]})


def week_view(request):
    today = datetime.now().date()
    dates = [today + timedelta(days=i) for i in range(0, 7)]
    days = []

    for day in dates:
        days.append({
            'day': day,
            'events': Event.objects.filter(date_time__year=day.year,
                                              date_time__month=day.month,
                                              date_time__day=day.day).order_by("date_time")
        })

    return render(request, "eventsapp/event_list.html", {"days": days})

def logout_view(request):
    logout(request)
    return redirect("/")

def calendar_list_view(request):
    return render(request, "eventsapp/list.html", {
        "events": Event.objects.all().order_by("date_time")
    })

@login_required
def submit_event_view(request):
    #form = EventForm(data=request.POST)
    #form.fields['club'].queryset = request.user.club_set.all()
    form = get_event_form(request.user.club_set.all(), request.POST)

    if form.is_valid():
        e = Event()
        e.description = form.cleaned_data['description']
        e.name = form.cleaned_data['name']
        e.date_time = form.cleaned_data['date']
        if form.cleaned_data['club']:
            e.club = form.cleaned_data['club']
            e.user_type = 'C'
        else:
            print(form.cleaned_data)
            e.user_type = 'U'
            e.user = request.user
        e.save()
        return redirect("/calendar/list")
    form = get_event_form(request.user.club_set.all())
    #form.fields['club'].queryset = request.user.club_set.all()
    return render(request, "eventsapp/submit.html", {"form": form})


def tests_view(request):
    # Insert events in two different dates to test day_view
    c1 = Club()
    c1.name="Sigma Phi"
    c1.creator=request.user
    c1.save()

    c2 = Club()
    c2.name="UVM Program Board"
    c2.creator= request.user
    c2.save()

    c3 = Club()
    c3.name="UVM CS Crew"
    c3.creator=request.user
    c3.save()

    #
    e = Event()
    e.description = "Students will be able to make 'blessing bags' full of necessities for COTS Homeless Shelter during the week of Random Acts of Kindness on Wednesday, April 6th at 7:30 PM. FeelGood will also be at the event, giving away 70 of their famous sammies for FREE, including crowd favorite, the Bella!"
    e.name = "Sammie's Spread Smiles!"
    e.user = request.user
    e.club = c2
    #April 6, 2016 7:30pm
    e.date_time = datetime.strptime("Apr 6 2016 7:30PM",'%b %d %Y %I:%M%p')
    e.save()

    # Event that should
    e1 = Event()
    e1.description = "Join other Catamounts from around campus at Brennan's Pub for an evening of trivia and prizes. Form a team, compete, and win yourselves some cool swag! And don't miss out on the food specials - $1.00 French Fries and $3.00 Milkshakes. P.S. Wicked Wednesday Pub Quiz happens in Brennan's EVERY Wednesday throughout the semester! Come back each week for trivia, prizes & food specials! Please contact the UVM Program Board (UPB) atupb@uvm.edu for questions and accommodations."
    e1.name = "Wicked Wednesday Pub Quiz"
    e1.club =  c2
    e1.user = request.user
    #April 6, 2016 9:00pm
    e1.date_time = datetime.strptime("Apr 6 2016 9:00PM",'%b %d %Y %I:%M%p')
    e1.save()

    # Event that should not show up for this week
    e2 = Event()
    e2.description = "Getting excited for this summer's superhero movie blockbusters coming to the big scren?! So are we! Come join us for three movie nights in Brennan's Pub at 8:00PM on three 'Super Thursdays' throughout April. We will be screening the first movies of three of your favorite Marvel Superheros beginning with: IRONMAN on April 7th, THOR on April 14th, & CAPTAIN AMERICA on April 21st. Hope to see you all there! Presented by UVM After Dark"
    e2.name = "UVM After Dark: Super Thursdays"
    e2.user = request.user
    e2.club = c2
    #April 7, 2016 8:00pm
    e2.date_time = datetime.strptime("Apr 2 2016 8:00PM",'%b %d %Y %I:%M%p')
    e2.save()

    e3 = Event()
    e3.description = "In this series, we ask UVM faculty & staff to think deeply about what matters to them, and provide a forum for them to lecture on a topic of their choosing, as if it were their last time to do so. The content of these lectures can vary, ranging from emotional to entertaining, but the underlying question is the same: What wisdom would you try to impart to the world if you knew it was your last chance?"
    e3.name = "UPB Presents: Last Lecture"
    e3.user = request.user
    e3.club = c2
    #April 13, 2016 7:00pm
    e3.date_time = datetime.strptime("Apr 8 2016 7:00PM",'%b %d %Y %I:%M%p')
    e3.save()

    e4 = Event()
    e4.description = "Meet at the gym for some b-ball"
    e4.name = "Pick up BasketBall game"
    e4.user = request.user
    #April 3, 12:00pm
    e4.date_time = datetime.strptime("Apr 13 2016 12:00PM",'%b %d %Y %I:%M%p')
    e4.save()

    e5 = Event()
    e5.description = "Charity Event at the Boys and Girls Clubs in the North End"
    e5.name = "Sigma Phi Philanthropy Event"
    e5.user = request.user
    e5.club = c1
    e5.date_time = datetime.strptime("Apr 2 2016 7:00PM",'%b %d %Y %I:%M%p')
    e5.save()

    e6 = Event()
    e6.description = "Come to CS Crew and Code a project"
    e6.user = request.user
    e6.name = "CS Crew Project Night"
    e6.club = c3;
    e6.date_time = datetime.strptime("Apr 6 2016 6:30PM",'%b %d %Y %I:%M%p')
    e6.save()


    return redirect("/")
