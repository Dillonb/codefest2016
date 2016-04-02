from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    if request.user.is_authenticated():
        return redirect("/calendar")
    else:
        return redirect("/accounts/login")

#@login_required
def account_view(request):
    return render(request, "eventsapp/account.html")

def logout_view(request):
    pass
