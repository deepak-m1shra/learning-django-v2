from django.shortcuts import render, redirect

from meetups.forms import RegistrationForm
from .models import Meetup, Participant
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
        if request.method == 'GET':
            print("GET METHOD")
            print("request" + str(request))
            registration_form = RegistrationForm()
            
        else:
            print("POST METHOD")
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)
            
        return render(request, 'meetups/meetup_details.html', 
                      { 
                        'meetup': selected_meetup, 
                        'found': True,
                        'form': registration_form
                        }
                      )
        
    except Exception as ex:
        print("Exception occured:::::"+ ex)
        return render(request, 'meetups/meetup_details.html', { 'found': False })
    

def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration_success.html', {'email': meetup.organizer})