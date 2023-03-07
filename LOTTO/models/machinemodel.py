from LOTTOAPI.basemodel import TimeBaseModel
from django.db import models


class MachineNumber(TimeBaseModel):
    name        = models.CharField(max_length=10, default='draw numbers', blank=True, null=True)
    monday      = models.CharField(max_length=3)
    tuesday     = models.CharField(max_length=3)
    wednesday   = models.CharField(max_length=3)
    thursdayday = models.CharField(max_length=3)
    friday      = models.CharField(max_length=3)

    def __str__(self):
        return self.name
