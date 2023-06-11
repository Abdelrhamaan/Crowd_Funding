from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import *

# class MyModelForm(forms.ModelForm):
#     class Meta:
#         model = user_reg
#         fields = ('profile_pic',)

class profile_edit_form(UserChangeForm):
    class Meta:
        model = user_reg
        exclude = ['email' , 'activated']

