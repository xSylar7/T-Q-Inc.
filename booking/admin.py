from django.contrib import admin
from .models import Event

# Register your models here.
# admin.site.register(Event)


@admin.register(Event)
class EventAdmin (admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'image',
        'organizer',
        'seats',
        'price',
        'seats_booked',
        'date_event',
    )
    readonly_fields = (
        'date_created',
    )
