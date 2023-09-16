from django.shortcuts import render
from django.http import HttpResponse
from .models import Meetup
# Create your views here.
def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {'meetups' : meetups})

def static(request):
    return render(request, 'meetups/index.html')

def meetup_details(request, meetup_slug):
    print(f"Meetup slug is::: {meetup_slug}")
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        return render(request, 'meetups/meetup_details.html', { 'meetup': selected_meetup, 'found': True })
    except Exception as ex:
        return render(request, 'meetups/meetup_details.html', { 'found': False })