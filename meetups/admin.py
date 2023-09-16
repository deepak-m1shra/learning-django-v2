from django.contrib import admin
from .models import Meetup
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'location')
    list_filter = ('title', 'location')
    prepopulated_fields = {'slug': ('title', 'location')}

admin.site.register(Meetup, MeetupAdmin)