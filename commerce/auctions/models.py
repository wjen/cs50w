from django.contrib.auth.models import AbstractUser
from django.db import models

# Inherits from abstractuser


class User(AbstractUser):
    pass


class Listing(models.Model):
    title: models.CharField(max_length=64)
    description: models.CharField(max_length=128, blank=True)
    image: models.URLField("Image URL Address", blank=True)
    price: models.DecimalField(decimal_places=2)
    user: models.ForeignKey(User, on_delete=models.CASCADE)
    date_added: models.DateField("date added", auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment: models.CharField(max_length=300)
    user: models.ForeignKey(User, on_delete=models.CASCADE)
    listing: models.ForeignKey(Listing, on_delete=models.CASCADE)
    date_added: models.DateField("date added", auto_now_add=True)

    def __str__(self):
        return f"{self.listing} -> {self.user}"


class Bid(models.Model):
    value: models.DecimalField(decimal_places=2)
    user: models.ForeignKey(User, on_delete=models.CASCADE)
    listing: models.ForeignKey(Listing, on_delete=model.CASCADE)
    date_added: models.DateField("date added", auto_now_add=True)

    def __str__(self):
        return f"{self.listing} -> {self.user}({self.value})"
