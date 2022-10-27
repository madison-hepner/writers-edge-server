from django.db import models
from .prompt import Prompt
from .prompt_type import Prompt_Type
from .WEUser import WEUser
from datetime import datetime

class PromptPost(models.Model):
    title = models.CharField(max_length=55)
    content = models.CharField(max_length=270)
    promptId = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    prompt_typeId = models.ForeignKey(Prompt_Type, on_delete=models.CASCADE)
    weuser = models.ForeignKey(WEUser, on_delete=models.DO_NOTHING)