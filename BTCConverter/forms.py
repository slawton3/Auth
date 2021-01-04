from django import forms
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


