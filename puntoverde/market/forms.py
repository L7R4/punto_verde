from django import forms
from .models import PersonVote

class VoteForm(forms.ModelForm):
    class Meta:
        model = PersonVote
        fields =[
            'vote',
        ]

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = PersonVote
        fields =[
            'number',
        ]