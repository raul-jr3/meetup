from django.contrib import admin

# Register your models here.
from .models import Meetup

class MeetupAdmin(admin.ModelAdmin):
    list_display = ['meetup_name', 'created_by', 'meetup_time', 'meetup_place',
                    'meetup_image', 'description']
    list_filter = ['created_by', 'meetup_time']

admin.site.register(Meetup, MeetupAdmin)
