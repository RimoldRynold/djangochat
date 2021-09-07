from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name

class Message(models.Model):
    value = models.TextField()
    date = models.DateTimeField(default=datetime.now , blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)

    # def __str__(self):
    #     return self.