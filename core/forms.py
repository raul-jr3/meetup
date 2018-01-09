from django import forms


from .models import Meetup

class CreateMeetupForm(forms.ModelForm):
    class Meta:
        model = Meetup
        fields = ['meetup_name', 'meetup_image', 'description', 'meetup_time', 'meetup_place', 'active']
