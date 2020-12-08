from django.db import models

# Create your models here.

class Mercury(models.Model):
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    standard = models.PositiveSmallIntegerField()
    marks = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name



