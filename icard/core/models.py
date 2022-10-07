from unittest.util import _MAX_LENGTH
from xml.parsers.expat import model
from django.db import models

# Create your models here.
from django.db import models


class comuna(models.Model):
    nombre = models.CharField(max_length=30)
