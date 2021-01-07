from django.views import View
from django.shortcuts import render
from .forms import ConvertForm
from blockchain import statistics, exchangerates
import json
import requests

class Home(View):
    def get(self, request):
        currList = []
        tickerList = []
        convertForm = ConvertForm()
        stats = statistics.get()
        ticker = exchangerates.get_ticker()
        for i in ticker:
            currList.append(i)
            tickerList.append(ticker[i])
        print(currList)
        print(tickerList)
        return render(request, 'BTCConverter/index.html', {'convertForm': convertForm, "currList": currList, "tickerList": tickerList})

    def post(self, request):
        convertForm = ConvertForm()
        c = ConvertForm(request.POST)
        url = "https://api.coingecko.com/api/v3"
        if c.is_valid():
            curr = c.cleaned_data['currency']
            amount = c.cleaned_data['amount']
            response = requests.get('https://blockchain.info/tobtc?currency={curr}&value={amount}'.format(curr=str(curr), amount=str(amount)))
            conversionVal = response.text
            print(conversionVal)
            return render(request, 'BTCConverter/index.html', {'convertForm': convertForm, 'conversionVal': conversionVal})