from django.db import models

# Create your models here.


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    # check out djangos website for info
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
# after finish with model, run python manage.py makemigrations, (create a migration to tell django to what changes to apply to database)
# then to migrate, run python mangage.py migrate
# python manage.py shell


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # blank true if passenger has no flight
    # if you have flight you can use passenger to access passengers
    flights = models.ManyToManyField(
        Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
