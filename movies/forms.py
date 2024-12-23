from django import forms
from .models import Comment, Movie
from .models import RoleUser


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = RoleUser
        fields = ['username', 'email', 'password']

class ModeratorRegisterForm(forms.ModelForm):
    class Meta:
        model = RoleUser
        fields = ['username', 'email', 'password']

class MovieRegisterForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'genre', 'year', 'image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
