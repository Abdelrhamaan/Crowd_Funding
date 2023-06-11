from django import forms
from .models import *

class MyModelForm(forms.ModelForm):
    class Meta:
        model = user_reg
        fields = ('profile_pic',)
