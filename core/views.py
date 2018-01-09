from django.shortcuts import render, get_object_or_404, redirect


from .models import Meetup
from .forms import CreateMeetupForm

# Create your views here.
def home(request):
    meetups = Meetup.objects.filter(active = True).order_by('-created')
    return render(request, 'core/home.html', {'meetups':meetups})

def meetup_detail(request, meetup_id):
    meetup = get_object_or_404(Meetup, id = meetup_id)
    #TODO : try taking all the meetups and putting it in the sidebar
    return render(request, 'core/meetup_detail.html', {'meetup':meetup})

def create_meetup(request):
    if request.method == 'POST':
        form = CreateMeetupForm(data = request.POST, files = request.FILES)

        if form.is_valid():
            new_meetup = form.save(commit = False)
            new_meetup.created_by = request.user
            new_meetup.save()
            return render(request, 'core/created.html', {'new_meetup':new_meetup})

    else:
        form = CreateMeetupForm()
    return render(request, 'core/create_meetup.html', {'form':form})

def edit_meetup(request, meetup_id):

    meetup = get_object_or_404(Meetup, id = meetup_id)

    if request.method == 'POST':
        form = CreateMeetupForm(instance = meetup, data = request.POST, files = request.FILES)

        if form.is_valid():
            form.save()
            return redirect('core:home')

    else:
        form = CreateMeetupForm(instance = meetup)
    return render(request, 'core/create_meetup.html', {'form':form, 'meetup':meetup})
