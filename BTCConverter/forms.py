from django import forms
from .models import Signup
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _


currencyTypes = [('USD', 'USD'),
                ('EUR', 'EUR'),
                ('CAD', 'CAD'),
                ('GBP', 'GBP'),
                ('AUS', 'AUS'),
                ('NZD', 'NZD'),
                ('CHF', 'CHF'),
                ('JPY', 'JPY')]

class ConvertForm(forms.Form):
    amount = forms.IntegerField()
    currency = forms.ChoiceField(required=True, choices=currencyTypes)


class EmailSignupForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={
        "type": "firstName",
        "name": "firstName",
        "id": "firstName",
        "placeholder": "First Name"
    }), label="")
    lastName = forms.CharField(widget=forms.TextInput(attrs={
        "type": "lastName",
        "name": "lastName",
        "id": "lastName",
        "placeholder": "Last Name"
    }), label="")
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Enter your email"
    }), label="")
    class Meta:
        model = Signup
        fields = ('firstName', 'lastName', 'email', )
