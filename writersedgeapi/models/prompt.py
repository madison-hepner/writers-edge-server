from django.db import models
from .prompt_type import Prompt_Type

class Prompt(models.Model):
        title = models.CharField(max_length=55)
        prompt_typeId = models.ForeignKey(Prompt_Type, on_delete=models.CASCADE)
        