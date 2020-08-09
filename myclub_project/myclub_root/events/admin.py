from django.contrib import admin
from events.models import Event, Venue, MyClubUser
# Register your models here.

# admin.site.register(Venue, VenueAdmin) is another way of registering
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')


class EventAdmin(admin.ModelAdmin):
    # hides attendees field when not here, cannot hide req fields
    # fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'description')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
    fieldsets = (
        ('Required Information', {
            'description': "These fields are required for each event.",
            'fields': (('name', 'venue'), 'event_date')
        }),
        ('Optional Information', {
            # Adds the collapse class to the fieldset.
            'classes': ('collapse',),
            'fields': ('description', 'manager')
        }),
    )


# admin.site.register(Venue)
# admin.site.register(Event)
admin.site.register(Event, EventAdmin)
admin.site.register(MyClubUser)
