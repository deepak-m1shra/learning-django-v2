from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    meetups = [
        {'title': 'First Meetup'},
        {'title': 'Second Meetup'},
        {'title': 'Third Meetup'}
    ]
    return render(request, 'meetups/static.html', 
                  {'meetups' : meetups,
                   'show_meetups': True}
                  )

def static(request):
    return render(request, 'meetups/static.html')