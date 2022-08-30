from django.db import models

class PersonVote(models.Model):
    vote = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=18, null=True, default="")

    def __str__(self):
        return self.vote
