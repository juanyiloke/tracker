from django.shortcuts import render

import asyncio
import aiohttp
import json
import urllib.parse
import time
import pandas as pd
import requests
import math

#emails
import smtplib
from email.mime.text import MIMEText

# this is selected according to the drop down which chooses which ticker we are interested in.
# choose from ["ETHUSD", "BTCUSD", "SOLUSD"]
symbol_of_interest = "ETHUSD"

# this is selected from the database of values. Values are updated by the user.
# In the valueDB, we have a table which stores the PK to be the tickers.
# The data in this table will be the symbol (ticker), the ask price (int), timestamp, timestamp local,
# and email_sent (bool), the alert_value (int)
# value is the alert_value(s) for any of the tickers.
values = [3765.0]




def alert_process(parsed_data=None, password='***REMOVED***', email='lokejuanyi@gmail.com'):
    """
    takes parsed data and sends an alert to specified email that ticker in parsed data has hit a
    specific ask price in the parsed_data, then removes the visibility of the ticker alert
    in the app.
    """
    # 1) Send email alert.
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    subject = 'check the price'
    body = 'bruh'
    msg = f'subject: {subject} {body}'
    server.sendmail(
        email,
        email,
        msg
    )
    print('email sent')
    server.quit()

    # 2) Remove visibility of the ticker alert from the UI.


def parse_ask_price(price):
    """
    Created because it is unlikely to receive the exact dollar and cents so we just parse to the nearest dollar.
    :param price: the ask price (float)
    :return: the price parsed to the nearest whatever.
    """
    frac, whole = math.modf(price)
    return whole


async def receive_required_data():
    # based on the API, all we need is the quotes data type.
    data_types = ["quotes"]
    stream_options = [
        {
            "exchange": "binance-us",
            "symbols": ["ETHUSD"],
          "dataTypes": data_types,
        },
        {
            "exchange": "binance-us",
            "symbols": ["BTCUSD"],
            "dataTypes": data_types,
        },
        {
            "exchange": "binance-us",
            "symbols": ["SOLUSD"],
            "dataTypes": data_types,
        },
    ]

    options = urllib.parse.quote_plus(json.dumps(stream_options))

    URL = f"ws://localhost:8001/ws-stream-normalized?options={options}"
    # real-time normalized data for two exchanges via single connection
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(URL) as websocket:
            async for msg in websocket:
                parsed_data = json.loads(msg.data)
                # this is for filtering for tickered data
                if parsed_data['symbol'] == symbol_of_interest:
                    for value in values:
                        ticker = parsed_data['symbol']
                        ask_price = parsed_data['asks'][0]['price']
                        print(f'Ask price for {ticker} at {ask_price}')
                        if parse_ask_price(ask_price) == value:
                            alert_process(parsed_data, '***REMOVED***')
                    print(parsed_data)
                    return parsed_data


if __name__ == "__main__":
    alert_process('NULL','***REMOVED***')
    # while True:
    #     asyncio.run(receive_required_data())
    #     # time.sleep(5)


# Create your views here.




