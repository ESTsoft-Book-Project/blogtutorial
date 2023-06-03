"""fields to fill out from users
"""

from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegisterForm(UserCreationForm):
    """pre-built user registration forms.... SICK!"""

    email = forms.EmailField()
    nickname = forms.CharField(max_length=255)

    class Meta:
        """details"""

        model = User
        fields = ["email", "nickname", "password1", "password2"]


class UserUpdateForm(UserChangeForm):
    """TODO: impl"""

    pass
