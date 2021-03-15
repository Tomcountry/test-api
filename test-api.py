import ccxt
import pandas as pd
import time

apiKey = "eqg-7JV0"
secret = "lPj4ExgDKshIZE_7BlKAt-GDbKeZyZVPQQ--xzG00xg"
exchange = ccxt.deribit({'apiKey': apiKey ,'secret': secret,'enableRateLimit': True,"urls": {"api": "https://test.deribit.com"}})


dfMatchOrder1 = pd.DataFrame(exchange.fetchMyTrades("BTC-PERPETUAL",limit=3),
                                 columns=['id', 'datetime', 'symbol', 'side', 'price', 'amount', "fee"])

while True:
    print(dfMatchOrder1)
    time.sleep(5)