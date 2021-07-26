from django.conf import settings
from django.db import models


class Platforms(models.Model):
    "Generated Model"
    site = models.URLField()
    logo = models.URLField()
    name = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )
