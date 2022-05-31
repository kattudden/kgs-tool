from django.shortcuts import render
from django.http import HttpResponse
from .models import Location
from .models import Building
from .models import Contact
from .models import Room
from .models import Item


def index(request):
    locations = Location.objects.all()
    context = {"locations": locations, "MEDIA_URL": "media/"}
    return render(request, 'locations.html', context)


def report_location(request, kgsId):
    location = Location.objects.get(id=kgsId)
    context = {
        "MEDIA_URL": "/media/",
        "location": location,
        "contacts": Contact.objects.filter(location=location.id),
        "buildings": Building.objects.filter(location=location.id),
        "rooms": Room.objects.filter(location=location.id),
        "items": Item.objects.filter(location=location.id)
    }
    return render(request, 'report.html', context)
