from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip/Post Code', max_length=12)
    phone = models.CharField('Contact Phone', max_length=20, blank=True)
    web = models.URLField('Web Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)

    def __str__(self):
        return self.name

# urlfield and emailfield specific to django advantage, otherwise would be varchar in sqlite
# django models provide built in validation for specialized fields


class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    # venue1 = Venue.objects.get(name="East Park"), retrieve first in shell to use ex. venue =venue1
    venue = models.ForeignKey(
        Venue, blank=True, null=True, on_delete=models.CASCADE)
    # The on_delete option is set to SET_NULL so if a user is deleted, all events they managed have their manager ID set to NULL.
    manager = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
