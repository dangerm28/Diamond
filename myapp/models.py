from django.db import models
from .abstracts import TimestampedModel


class MyModel(TimestampedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
