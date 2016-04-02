from django import forms
from django.forms import ModelForm
from eventsapp.models import *

class EventForm(ModelForm):
    name = forms.CharField(required=True)
    description = forms.CharField(required=True)
    class Meta:
        model = Event
        fields = ['description', 'name']
