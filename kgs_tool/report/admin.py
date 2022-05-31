from django.contrib import admin
from .models import Location
from .models import Building
from .models import Contact
from .models import Room
from .models import Item


class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "gemeinde", "plz")


class BuildingAdmin(admin.ModelAdmin):
    list_display = ("name", "hausnummer", "location")


class ContactAdmin(admin.ModelAdmin):
    list_display = ("vorname", "nachname", "mobile", "location", "bemerkungen")


class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "building", "location")


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "room", "priority")


# Register your models here.
admin.site.register(Location, LocationAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Item, ItemAdmin)
