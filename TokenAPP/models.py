from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=50, null=False)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=200, default="", null=True)

    def __str__(self):
        return "{} -{}".format(self.username, self.email)
