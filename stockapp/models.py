# stockapp/models.py

from django.db import models

class StockNews(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  timestamp = models.DateTimeField()
