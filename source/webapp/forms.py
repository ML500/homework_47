from django import forms
from .models import STATUS_CHOICES

default_status = STATUS_CHOICES[0][0]


class GoalForm(forms.Form):
    describe = forms.CharField(max_length=200, required=True, label='Description')
    detail = forms.CharField(max_length=3000, required=True, label='Detail', widget=forms.Textarea)
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=default_status, label='Moderation')
