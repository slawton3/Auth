from django.views import View
from django.shortcuts import render
from .forms import ConvertForm
import requests

class Home(View):
    def get(self, request):
        convertForm = ConvertForm()
        return render(request, 'BTCConverter/index.html', {'convertForm': convertForm})

    def post(self, request):
        convertForm = ConvertForm()
        c = ConvertForm(request.POST)
        if c.is_valid():
            curr = c.cleaned_data['currency']
            amount = c.cleaned_data['amount']
            response = requests.get('https://blockchain.info/tobtc?currency={curr}&value={amount}'.format(curr=str(curr), amount=str(amount)))
            conversionVal = response.text
            print(conversionVal)
            return render(request, 'BTCConverter/index.html', {'convertForm': convertForm, 'conversionVal': conversionVal})