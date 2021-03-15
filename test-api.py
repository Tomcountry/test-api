import ccxt
import pandas as pd
import time
import json
import csv
import os
from os import environ
import requests


joker = environ["api"]
batman = environ["secret"]
apiKey = "eqg-7JV0"
secret = "lPj4ExgDKshIZE_7BlKAt-GDbKeZyZVPQQ--xzG00xg"
exchange = ccxt.deribit({'apiKey': apiKey ,'secret': secret,'enableRateLimit': True,"urls": {"api": "https://test.deribit.com"}})

pair = "BTC-PERPETUAL"
size_order = 10 # USD
types = 'limit'
side = 'buy'
price = 1000
postOnly =  False
reduceOnly = False
ioc = False
timestampUntil = 1615184598249

dfZone = pd.read_csv("ZoneTestCSV.csv")
dfTransaction = pd.read_csv("TransactionTestCSV.csv")

#ราคาตลาด (ต้องแก้ไข)
r1 = json.dumps(exchange.fetch_ticker('BTC-PERPETUAL'))
dataPriceBTC = json.loads(r1)
MarketPrice = dataPriceBTC['last']
print('BTC-PERPETUAL=',MarketPrice,'$')


