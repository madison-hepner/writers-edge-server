from django.db import models
from django.contrib.auth.models import User


class WEUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)