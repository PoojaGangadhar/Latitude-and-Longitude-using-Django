from django.db import models


# Create your models here.
class TemperatureData(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()

    def __str__(self):
        return f'Temperature reading at {self.timestamp}:{self.temperature}'
