from django.db import models

# Create your models here.


class Calibration(models.Model):
    description = models.TextField(max_length=500)
