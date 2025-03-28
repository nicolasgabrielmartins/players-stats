from django.db import models

# Create your models here.
class Players(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    minutes_played = models.FloatField()
    wins = models.IntegerField()
    loses = models.IntegerField()
    points_per_game = models.FloatField()