from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=200, null=False, blank=True, unique=True)
    email = models.EmailField(max_length=200, null=False)
    age = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} -{}".format(self.username, self.email)
