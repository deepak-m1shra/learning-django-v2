from django.contrib import admin
from .models import Meetup, Location, Participant
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'location')
    list_filter = ('title', 'location')
    prepopulated_fields = {'slug': ('title', 'location')}
    
class LocationAdmin(admin.ModelAdmin):
    list_display = ('location', 'address')
    list_filter = ('location')


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)