from django import forms
from django.forms import ModelForm
from eventsapp.models import *
import datetime
def get_event_form(clubs, data=None):
    class EventForm(ModelForm):
        name = forms.CharField(required=True)
        description = forms.CharField(required=True)
        date = forms.DateTimeField(initial=datetime.datetime.now(), widget=forms.DateTimeInput(), required=True)
        club = forms.ModelChoiceField(required=False, queryset=clubs)

        class Meta:
            model = Event
            fields = ['name', 'description', 'date', 'club']
    if data:
        return EventForm(data=data)
    else:
        return EventForm()

class ClubForm(ModelForm):
    name = forms.CharField(required=True)
    class Meta:
        model = Club
        fields = ['name']
