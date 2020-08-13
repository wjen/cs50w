from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Inherits from abstractuser

class User(AbstractUser):
    pass


class Listing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=128, blank=True)
    image = models.URLField("Image URL Address", blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateField("date added", auto_now_add=True)

    def __str__(self):
        return self.title


class Bid(models.Model):
    added_date = models.DateField("date added", auto_now_add=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    listing = models.ForeignKey(
        'Listing', on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='my_bids')

    def __str__(self):
        return f"{self.listing} -> {self.user}({self.value})"


class Comment(models.Model):
    added_date = models.DateField("date added", auto_now_add=True)
    entry = models.TextField()
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.listing} -> {self.user}: {self.entry}"
