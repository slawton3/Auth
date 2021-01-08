from django.views import View
from django.shortcuts import render
from .forms import ConvertForm
from blockchain import statistics, exchangerates
import pandas as pd
import json
import requests

class Home(View):
    def get(self, request):
        currList = []
        buyList = []
        sellList = []
        past15 = []
        cols = ["Currency", "Last Buy Price", "Last Sell Price", "Price 15 Mins Ago"]
        convertForm = ConvertForm()
        stats = statistics.get()
        ticker = exchangerates.get_ticker()
        for i in ticker:
            currList.append(i)
            buyList.append(ticker[i].buy)
            sellList.append(ticker[i].sell)
            past15.append(ticker[i].p15min)

        data = {cols[0]: currList,
                cols[1]: buyList,
                cols[2]: sellList,
                cols[3]: past15}
        df = pd.DataFrame(data, columns=cols)
        htmlTable = df.to_html(index=False, classes="table, exchangeRates")
        print(htmlTable)
        return render(request, 'BTCConverter/index.html', {'convertForm': convertForm, "htmlTable": htmlTable})

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