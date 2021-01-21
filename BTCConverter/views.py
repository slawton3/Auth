from django.views import View
from django.shortcuts import render
from django.contrib import messages
from .forms import ConvertForm, EmailSignupForm
from .models import Signup
from blockchain import statistics, exchangerates
import pandas as pd
from django.conf import settings
import json
import requests


MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = 'https://{dc}.api.mailchimp.com/3.0'.format(dc=MAILCHIMP_DATA_CENTER)
members_endpoint = '{api_url}/lists/{list_id}/members'.format(
    api_url=api_url,
    list_id=MAILCHIMP_EMAIL_LIST_ID
)

class Home(View):
    def get(self, request):
        form = EmailSignupForm()
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
        return render(request, 'BTCConverter/index.html', {'convertForm': convertForm, "htmlTable": htmlTable, "emailForm": form})

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

def subscibe(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()

class Subscribe(View):
    def get(self, request):
        form = EmailSignupForm()
        return render(request, 'BTCConverter/subscribe.html', {"emailForm": form})

    def post(self, request):
        form = EmailSignupForm(request.POST or None)
        if form.is_valid():
            email_signup_queryset = Signup.objects.filter(email=form.instance.email)
            if email_signup_queryset.exists():
                messages.info(request, "You are already subscribed.")
            else:
                subscibe(form.instance.email)
                form.save()
        return render(request, 'BTCConverter/subscribe.html', {"emailForm": form})