from django.db import models

class TimeBaseModel(models.Model):
    event = models.CharField(max_length=10)
    date  = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        abstract = True
        