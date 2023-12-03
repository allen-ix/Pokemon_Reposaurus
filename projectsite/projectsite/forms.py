# forms.py
from django import forms
from cardquest.models import Trainer

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'birthdate', 'location', 'email'] 

class TrainerAddForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['name', 'birthdate', 'location', 'email']
