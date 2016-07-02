from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Show(models.Model):
    show_name = models.CharField(max_length=50)
    show_info = models.CharField(max_length=300)
    show_type = models.IntegerField()
    show_cost = models.IntegerField()
    show_image = models.ImageField()

    def __str__(self):
        return self.show_name

class Stage(models.Model):
    stage_name = models.CharField(max_length=50)
    stage_info = models.CharField(max_length=300)
    stage_image = models.ImageField()
    stage_shows = models.ManyToManyField(Show)

    def __str__(self):
        return self.stage_name

class Venue(models.Model):
    venue_name = models.CharField(max_length=50)
    venue_info = models.CharField(max_length=300)
    venue_location = models.CharField(max_length=100)
    venue_stages = models.ManyToManyField(Stage)

    def __str__(self):
        return self.venue_name

