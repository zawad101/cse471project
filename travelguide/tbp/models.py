from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class traveler(AbstractUser):
    username = models.CharField(max_length=150, primary_key=True)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(null=True)
    age = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.username

