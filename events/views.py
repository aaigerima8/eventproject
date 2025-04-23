from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Event

def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})
