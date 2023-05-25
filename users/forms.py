"""fields to fill out from users
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """pre-built user registration forms.... SICK!"""
    email = forms.EmailField()

    class Meta:
        """details"""
        model = User
        fields = ['username', 'email', 'password1', 'password2']
