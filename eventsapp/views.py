from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def home_view(request):
    if request.user.is_authenticated():
        return redirect("/calendar")
    else:
        return redirect("/accounts/login")

def logout_view(request):
    pass
