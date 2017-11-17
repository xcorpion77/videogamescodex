"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Videogames(models.Model):
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=20)
    year = models.IntegerField()
    GENRES = (
        (0, "Action"),
        (1, "Adventure"),
        (2, "Strategy"),
        (3, "RPG"),
        (4, "Sport")
        )
    genre = models.IntegerField(choices = GENRES)
    PLATFORMS = (
        (0, "PC"),
        (1, "PS4"),
        (2, "XBOX ONE")
        )
    platform = models.IntegerField(choices = PLATFORMS)
    score = models.IntegerField()
    online = models.BooleanField()
    PEGI = (
        (0, "PEGI7"),
        (1, "PEGI16"),
        (2, "PEGI18")
        )
    pegi = models.IntegerField(choices = PEGI)