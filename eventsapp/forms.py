from django import forms
from django.forms import ModelForm
from eventsapp.models import *
import datetime

class EventForm(ModelForm):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True)
    date = forms.DateTimeField(initial=datetime.datetime.now(), widget=forms.DateTimeInput(), required=True)
    club = forms.ModelChoiceField(required=False, queryset=Club.objects.all())

    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'club']

class ClubForm(ModelForm):
    name = forms.CharField(required=True)
    class Meta:
        model = Club
        fields = ['name']
