'''Are gonna be Classes that take in a model that we want to serialize or object 
and its gonna turn it into json data from python data'''
from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

