from django import forms
from . import models

class studentForm(forms.ModelForm):
    class Meta:
        model = models.studentModel
        fields = '__all__'
        # fields = ['name', 'roll']
        # exclude = ['fathers_name']
        labels = {
            'name': 'student name',
            'roll': 'student roll'
        }
        help_texts = {
            'name':'please enter your name',
            'roll': 'please enter your roll'
        }
        