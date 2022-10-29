from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from booking.forms import EventForm
from .models import Event


# Create your views here.

def get_home(request):
    return render(request, 'index.html')


@login_required
def user_home(request):
    return render(request, 'user_home.html')


@login_required
def user_profile(request):
    return render(request, 'user_profile.html')


def get_events(require):
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
    context = {'events': _events}
    return render(require, 'user_home.html', context)


def create_event(require):
    form = EventForm()
    if require.method == 'POST':
        form = EventForm(require.POST)
        if form.is_valid():
            form.save()
            return redirect('user_home')
    context = {'form': form}
    return render(require, 'event_create.html', context)
