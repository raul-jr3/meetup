from django.shortcuts import render, get_object_or_404


from .models import Meetup

# Create your views here.
def home(request):
    meetups = Meetup.objects.filter(active = True).order_by('-created')
    return render(request, 'core/home.html', {'meetups':meetups})

def meetup_detail(request, meetup_id):
    meetup = get_object_or_404(Meetup, id = meetup_id)
    #TODO : try taking all the meetups and putting it in the sidebar
    return render(request, 'core/meetup_detail.html', {'meetup':meetup})
