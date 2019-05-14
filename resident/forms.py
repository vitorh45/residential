from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms.models import inlineformset_factory
from .models import Resident, HouseResident, VehicleResident
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset
from .formsets import Formset
from django.shortcuts import reverse


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
    email = forms.CharField(label='Email', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    cpf = forms.CharField(label='CPF', widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    birth_date = forms.DateField(label='Data de nascimento', input_formats=['%d/%m/%Y'])

    class Meta:
        model = Resident
        fields = ('email', 'cpf', 'rg', 'birth_date', 'lot_block', 'lot_number', 'street', 'number', 'cep')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_action = reverse('edit')
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-lg-6 mb-0'),
                Column('cpf', css_class='form-group col-lg-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('rg', css_class='form-group col-lg-6 mb-0'),
                Column('birth_date', css_class='form-group col-lg-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('lot_block', css_class='form-group col-lg-6 mb-0'),
                Column('lot_number', css_class='form-group col-lg-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('street', css_class='form-group col-lg-7 mb-0'),
                Column('number', css_class='form-group col-lg-2 mb-0'),
                Column('cep', css_class='form-group col-lg-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Fieldset('Adicionar moradores',
                         Formset('houses')),
                css_class='form-row'
            ),
            Row(
                Fieldset('Adicionar veículos',
                         Formset('vehicles')),
                css_class='form-row'
            ),
            Row(
                Submit('submit', 'Send', css_class='btn btn-primary btn-larger'),
                css_class='float-right form-row'
            ),
        )


class HouseResidentForm(forms.ModelForm):
    class Meta:
        model = HouseResident
        fields = ('name', 'birth_date',)


class VehicleResidentForm(forms.ModelForm):
    class Meta:
        model = VehicleResident
        fields = '__all__'


HouseResidentnFormset = inlineformset_factory(Resident, HouseResident, form=HouseResidentForm, extra=2)
VehicleResidentnFormset = inlineformset_factory(Resident, VehicleResident, form=VehicleResidentForm, extra=2)
