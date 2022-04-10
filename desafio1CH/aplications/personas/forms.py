from django import forms

from .models import Familiar

class FamiliarForm(forms.ModelForm):

    class Meta:
        model = Familiar
        fields = (
        'first_name', 
        'last_name',
        'birthday',
        'age', 
        'relative', 
        'foto',
        'hobbies',
        'bio'
    )
        widgets = {
            'hobbies': forms.CheckboxSelectMultiple()
        }