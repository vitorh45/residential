from django import forms
from .models import Resident


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = ('first_name', 'last_name', 'email', 'cpf', 'lot', 'password')