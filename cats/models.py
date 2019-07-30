from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Cat(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    created_date = models.DateTimeField(default=timezone.now)


def __str__(self):
    return self.name
