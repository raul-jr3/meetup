from django.shortcuts import render


from .models import Meetup

# Create your views here.
def home(request):
    meetups = Meetup.objects.filter(active = True).order_by('-created')
    return render(request, 'core/home.html', {'meetups':meetups})
