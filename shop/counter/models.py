from django.contrib.auth.models import User
from django.db import models


class VisitsCounter(models.Model):
    """The model for counting page visits by registered users"""
    path = models.CharField(max_length=500)
    counter = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.user} | {self.path} | {self.counter}'
