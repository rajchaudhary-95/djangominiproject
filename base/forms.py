from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'      # Gives all the fields from models.py class Room 
        exclude = ['host','participants']