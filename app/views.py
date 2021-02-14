from django.shortcuts import render

# Create your views here.
from .models import Event
def index(request):
	events = Event.objects.all()
	return render(request, "index.html",{"events":events})