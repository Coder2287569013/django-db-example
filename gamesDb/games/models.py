from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ManyToManyField("Genre", related_name="genres")
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name