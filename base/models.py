from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #it could be null and also be kept empty and changed afterwards
    participants = models.ManyToManyField(User, related_name='participants', blank = True)
    updated = models.DateTimeField(auto_now=True) #it takes the snapshot of everytime this table is updated
    created = models.DateField(auto_now_add=True) #it takes snapshot of time the first time the table was created(instance of this class was created)

    class Meta:
        ordering = ['-updated', '-created']     #normal updated and created does ascending order and with a - minus it does descending order

    def __str__(self):
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)   #If a Room is deleted, all related Message objects are automatically deleted too.
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #it takes the snapshot of everytime this table is updated
    created = models.DateField(auto_now_add=True) #it takes snapshot of time the first time the table was created(instance of this class was created)
    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return self.body[0:50]