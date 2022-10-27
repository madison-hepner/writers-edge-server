from django.db import models
from .WEUser import WEUser

class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.CharField(max_length=270)
    weuser = models.ForeignKey(WEUser, on_delete=models.DO_NOTHING)