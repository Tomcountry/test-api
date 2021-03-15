import ccxt
import pandas as pd
import time
import os
from os import environ


apiKey = environ["api"]
secret = environ["secret"]
exchange = ccxt.deribit({'apiKey': apiKey ,'secret': secret,'enableRateLimit': True,"urls": {"api": "https://test.deribit.com"}})


dfMatchOrder1 = pd.DataFrame(exchange.fetchMyTrades("BTC-PERPETUAL",limit=3),
                                 columns=['id', 'datetime', 'symbol', 'side', 'price', 'amount', "fee"])

while True:
    print(apiKey)
    print(secret)
    print(dfMatchOrder1)
    time.sleep(5)