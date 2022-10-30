from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from booking.forms import EventForm
from .models import Event
from users.models import User


# Create your views here.

def get_home(request):
    return render(request, 'index.html')


@login_required
def user_home(request, user_id):
    user = User.objects.get(id=user_id)
    context = {"user": user}
    return render(request, 'user_home.html', context)


@login_required
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {"user": user}
    return render(request, 'user_profile.html', context)


def get_events(req):
    events = Event.objects.all()
    _events = []
    for event in events:
        _events.append(
            {
                'id': event.id,
                'name': event.name,
                'image': event.image,
                'organizer': event.organizer,
                'seats': event.seats,
                'price': event.price,
                'seats_booked': event.seats_booked,
                'date_event': event.date_event,
                'date_created': event.date_created,

            }
        )
    print(_events)
    context = {'events': _events}
    return render(req, 'user_home.html', context)


def get_event(req, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        "event": {
            "id": event.id,
            "name": event.name,
            "image": event.image,
            "organizer": event.organizer,
            "seats": event.seats,
            "price": event.price,
            "seats_booked": event.seats_booked,
            "date_event": event.date_event,
            "date_created": event.date_created,

        }
    }
    return render(req, "event_details.html", context)


def create_event(req):
    form = EventForm()
    if req.method == 'POST':
        form = EventForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('user-home')
    context = {'form': form}
    return render(req, 'event_create.html', context)
