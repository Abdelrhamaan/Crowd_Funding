from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import *


class profile_edit_form(UserChangeForm):
    password = forms.CharField()

    class Meta:
        model = user_reg
        exclude = ['email', 'activated']
