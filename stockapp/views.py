# stockapp/views.py

from django.shortcuts import render
import requests
from .models import StockNews
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta

def fetch_stock_news(request):
  api_key = settings.ALPHA_VANTAGE_API_KEY
  endpoint = 'https://www.alphavantage.co/query?'
  params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'IBM',  # Ändern Sie das Symbol entsprechend Ihrer Anforderungen
    'outputsize' : 'compact',
    #'interval': '5min',
    'apikey': api_key,
    'datatype' : 'json'
  }

  response = requests.get(endpoint, params=params)
  data = response.json()
  #news = StockNews.objects.all()

  return render(request, 'news.html', {'news': data})
