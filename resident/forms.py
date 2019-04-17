from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import Resident


class ResidentCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Resident
        fields = ('cpf', 'birth_date',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data['cpf']
        if commit:
            user.save()
        return user


class ResidentEditForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    birth_date = forms.DateField(label='Data de nascimento', input_formats=['%d/%m/%Y'])

    class Meta:
        model = Resident
        fields = ('email', 'cpf', 'rg', 'birth_date', 'lot_block', 'lot_number', 'street', 'number', 'cep')
