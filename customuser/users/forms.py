# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        #fields = UserCreationForm.Meta.fields

        # Django default fields are username and password, but we want to make sure our user has an email associated
        # with it. The reason we don't see the specify password is because Django automatically requires a password
        # by default
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        #fields = UserChangeForm.Meta.fields

        # Django default fields are username and password, but we want to make sure our user has an email associated
        # with it. The reason we don't see the specify password is because Django automatically requires a password
        # by default
        fields = ('username', 'email')

