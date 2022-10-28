from email.policy import default
from django.db import models

# Create your models here.


class Event(models.Model):

    name = models.CharField(max_length=50)
    image = models.ImageField()
    organizer = models.CharField(max_length=30)
    seats = models.PositiveIntegerField(default=0)
    price = models.CharField(max_length=30, blank=True, default="")
    seats_booked = models.PositiveIntegerField(default=0)
    date_event = models.DateField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
