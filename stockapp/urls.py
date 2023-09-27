# stockapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
  path('fetch_stock_news/', views.fetch_stock_news, name='fetch_stock_news'),
]
