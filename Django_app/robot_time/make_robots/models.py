from django.db import models
from django.utils import timezone


class Robot(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    strength = models.PositiveSmallIntegerField()
    armour = models.PositiveSmallIntegerField()
    agility = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    def updated(self):
        return timezone.now()

