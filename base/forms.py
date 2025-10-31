from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Message
from django import forms

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email','password1','password2']



class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'      # Gives all the fields from models.py class Room 
        exclude = ['host','participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username','email','bio']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Write your message here...',
                'rows': 3,
                'style': 'resize: vertical; min-height: 80px;'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = ""