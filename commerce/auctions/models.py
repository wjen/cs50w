from django.contrib.auth.models import AbstractUser
from django.db import models

# Inherits from abstractuser


class User(AbstractUser):
    pass


class Comment(models.Model):
    comment: models.CharField(max_length=300)
    commenter: models.ForeignKey(User, on_delete=models.CASCADE)
    listing: models.ForeignKey(Listing, on_delete=models.CASCADE)


class Bid(models.Model):
    price: models.IntegerField()
    bidder: models.ForeignKey(User, on_delete=models.CASCADE)
    listing: models.ForeignKey(Listing, on_delete=model.CASCADE)


class Listing(models.Model):
    title: models.CharField(max_length=64)
    description: models.CharField(max_length=128, blank=True)
    image: models.URLField("Image URL Address", blank=True)
    starting_bid: models.ForeignKey(Bid, on_delete=models.CASCADE)
    lister: models.ForeignKey(User, on_delete=models.CASCADE)
