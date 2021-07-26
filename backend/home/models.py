from django.conf import settings
from django.db import models


class Platforms(models.Model):
    "Generated Model"
    name = models.TextField()
    site = models.URLField()
    logo = models.URLField()
