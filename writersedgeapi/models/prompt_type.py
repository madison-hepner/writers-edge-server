from django.db import models

class Prompt_Type(models.Model):
    prompt_type = models.CharField(max_length=55)