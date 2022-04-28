# Apifiny OPEN API Connector Python


This is a library that works as a connector to [APIFINY OPEN API](https://github.com/Apifiny-IO/apifiny-connector-python)

- Supported APIs:
    - REST trading/market API


## OPEN API Documentation

[https://doc.apifiny.com/connect/#introduction](https://doc.apifiny.com/connect/#introduction)


## Install
```python
pip3 install apifiny
```

## RESTful APIs

Usage examples:
```python
from apifiny.rest_market import MarketData as MD_Client

md_client = MD_Client()
# Get BINANCE orderbook of BTCUSDT
print(client.market_order_book("BINANCE", "BTCUSDT"))
# Get BINANCE klines of BTCUSDT at 1m interval
print(md_client.market_kline("BINANCE", "BTC", "USDT", "1m"))
```

```python
from apifiny.rest_api import API as Client

client = Client(False,"BINANCE")
# Get server timestamp
print(client.server_time())

# api key/secret are required for user data endpoints
client = Client(unified_url=False, venue="BINANCE", account_id='<account_id>', key='<api_key>', secret='<api_secret>')

# Post a new order
params = {
    "accountId": account_id,
    "venue": "BINANCE",
    "orderId": "",
    "orderInfo": {
        "limitPrice": "30000",
        "orderSide": "BUY",
        "orderType": "LIMIT",
        "quantity": "0.0001",
        "symbol": "BTCUSDT",
        "timeInForce": 1,
    }
}

response = client.new_order(**params)
print(response)
```
Please find `examples` folder to check for more endpoints.


## Contributing

Contributions are welcome.<br/>
If you've found a bug within this project, please open an issue to discuss what you would like to change.<br/>
If it's an issue with the API, please new issue at [apifiny-connector-python issues](https://github.com/Apifiny-IO/apifiny-connector-python/issues)