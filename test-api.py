import ccxt
import pandas as pd
import time
import os



apiKey ="dasdasd"
secret = "dsadsadd"
exchange = ccxt.deribit({'apiKey': apiKey ,'secret': secret,'enableRateLimit': True,"urls": {"api": "https://test.deribit.com"}})


dfMatchOrder1 = pd.DataFrame(exchange.fetchMyTrades("BTC-PERPETUAL",limit=3),
                                 columns=['id', 'datetime', 'symbol', 'side', 'price', 'amount', "fee"])

while True:
    print(dfMatchOrder1)
    time.sleep(5)