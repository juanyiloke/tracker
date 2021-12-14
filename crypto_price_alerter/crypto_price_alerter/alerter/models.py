from django.db import models

# Create your models here.
from django.db import models

# this is selected from the database of values. Values are updated by the user.
# In the valueDB, we have a table which stores the PK to be the tickers.
# The data in this table will be the symbol (ticker), the ask price (int), timestamp, timestamp local,
# and email_sent (bool), the alert_value (int)
# value is the alert_value(s) for any of the tickers.

class Order(models.Model):
    ticker = models.CharField(max_length=20)
    alert_price = models.FloatField()
    email_sent = models.BooleanField()
    timestamp = models.DateField(auto_now=True)