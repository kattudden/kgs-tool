from django.db import models
from django.core.validators import RegexValidator


PRIORITIES = (
    (1, "1"),
    (2, "2"),
    (3, "3"),
    (4, "4"),
    (5, "5"),
)


KGS_ID_VALIDATOR = RegexValidator(r'^[A-Z]{1}\d{4}', 'not a valid kgs id')
STREET_VALIDATOR = RegexValidator(r'^\w+$', 'Nur den Strassennamen eingeben!')


def _location_file(instance, filename):
    return "location/{0}/{1}".format(
        instance.id, filename)


def _building_file(instance, filename):
    return "location/{0}/buildings/{1}/{2}".format(
        instance.location.id, instance.id, filename)


def _room_file(instance, filename):
    return "location/{0}/buildings/{1}/rooms/{2}/{3}".format(
        instance.location.id, instance.building.id, instance.id, filename)


def _item_file(instance, filename):
    return "location/{0}/buildings/{1}/rooms/{2}/{3}/{4}".format(
        instance.location.id,
        instance.building.id,
        instance.room.id,
        instance.id,
        filename)


class Location(models.Model):
    id = models.CharField(
        max_length=5,
        primary_key=True,
        validators=[KGS_ID_VALIDATOR])
    name = models.CharField(max_length=50)
    gemeinde = models.CharField(max_length=30)
    plz = models.IntegerField()
    ort = models.CharField(max_length=40, validators=[STREET_VALIDATOR])
    strasse = models.CharField(max_length=50, validators=[STREET_VALIDATOR])
    koordinaten = models.CharField(max_length=40)
    bild = models.FileField(upload_to=_location_file)
    karte = models.FileField(upload_to=_location_file)
    aufgenommen_am = models.DateField()

    def __str__(self):
        return f"{self.id}-{self.name}"


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    hausnummer = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    bild = models.FileField(upload_to=_building_file)
    karte = models.FileField(upload_to=_building_file)

    def __str__(self):
        return f"{self.name}-{self.location.strasse}, {self.hausnummer}"


class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    vorname = models.CharField(max_length=50)
    nachname = models.CharField(max_length=50)
    strasse = models.CharField(max_length=50)
    hausnummer = models.CharField(max_length=5)
    plz = models.IntegerField()
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    bemerkungen = models.TextField(null=True)

    def __str__(self):
        return f"{self.location.name} / {self.vorname}, {self.nachname}"


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    karte = models.FileField(upload_to=_room_file)

    def __str__(self):
        return f"{self.building.name} / {self.name}"


class Item(models.Model):
    id = models.CharField(
        max_length=5,
        primary_key=True,
        validators=[KGS_ID_VALIDATOR])
    name = models.CharField(max_length=50)
    aufgenommen_am = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    lage = models.CharField(max_length=50, blank=True)
    priority = models.IntegerField(choices=PRIORITIES, default=5, max_length=1)
    beschreibung = models.TextField()
    hoehe = models.CharField(max_length=50)
    tiefe = models.CharField(max_length=50)
    breite = models.CharField(max_length=50)
    feuer = models.BooleanField()
    wasser = models.BooleanField()
    gewalt = models.BooleanField()
    schmutz = models.BooleanField()
    massnahmen = models.TextField()
    personal = models.CharField(max_length=100)
    material = models.TextField(blank=True)
    evakuation = models.TextField(blank=True)
    plan = models.FileField(upload_to=_item_file)
    bild = models.FileField(upload_to=_item_file)

    def __str__(self):
        return f"{self.id} / {self.name}"
