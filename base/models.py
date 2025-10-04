from django.db import models

# Create your models here.

class Room(models.Model):
    #host =
    #topic =
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) #it could be null and also be kept empty and changed afterwards
    updated = models.DateTimeField(auto_now=True) #it takes the snapshot of everytime this table is updated
    created = models.DateField(auto_now_add=True) #it takes snapshot of time the first time the table was created(instance of this class was created)


    def __str__(self):
        return self.name