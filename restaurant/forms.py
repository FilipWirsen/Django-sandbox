from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=30, help_text='Required. Please provide a valid email adress.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')