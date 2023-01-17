from django.db import models
from datetime import datetime
class PersonVote(models.Model):
    date  = models.DateTimeField(auto_now_add = True)
    vote = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=18, null=True, default="")
    def __str__(self):
        return self.vote
