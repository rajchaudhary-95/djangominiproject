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
    is_code_snippet = forms.BooleanField(
        required=False, 
        label='Code Snippet',
        widget=forms.CheckboxInput(attrs={'class': 'code-snippet-toggle'})
    )
    language = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Select Language'),
            ('python', 'Python'),
            ('javascript', 'JavaScript'),
            ('html', 'HTML'),
            ('css', 'CSS'),
            ('java', 'Java'),
            ('cpp', 'C++'),
            ('sql', 'SQL'),
            ('bash', 'Bash/Shell'),
            ('json', 'JSON'),
            ('xml', 'XML'),
            ('markdown', 'Markdown'),
        ],
        widget=forms.Select(attrs={'class': 'language-select'})
    )
    
    class Meta:
        model = Message
        fields = ['body', 'file', 'is_code_snippet', 'language']