from django import forms
from .models import Event


class EventForm (forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'image', 'organizer', 'seats', 'price',
                  'seats_booked', 'date_event', ]
