# Apifiny OPEN API Connector Python


This is a library that works as a connector to [APIFINY OPEN API](https://github.com/Apifiny-IO/apifiny-connector-python)

- Supported APIs:
>- REST trading/market API
>- WebSocket trading/market API


## OPEN API Documentation

[https://doc.apifiny.com/connect/#introduction](https://doc.apifiny.com/connect/#introduction)


## Install
```python
pip3 install apifiny
```
Use windows, installing quickfix fails,Please use the link to download the file and install locally.
https://www.lfd.uci.edu/~gohlke/pythonlibs/#quickfix

## RESTful APIs
**Usage examples:**

Get all supported exchanges
```python
from apifiny.rest_api import API as Client

client = Client()
print(client.list_venue())
```
Get Market Data
```python
from apifiny.rest_market import MarketData as MD_Client

md_client = MD_Client()
# Get BINANCE orderbook of BTCUSDT
print(md_client.market_order_book("BINANCE", "BTCUSDT"))
# Get BINANCE klines of BTCUSDT at 1m interval
print(md_client.market_kline("BINANCE", "BTC", "USDT", "1m"))
```
Create Order
```python
from apifiny.rest_api import API as Client

client = Client(False,"BINANCE")
# Get server timestamp
print(client.server_time())

# api key/secret are required for trade endpoints
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
## WebSocket APIs

**Usage examples:**

Subscribe Market Data
```python
from apifiny.ac_websocket import ACSpotApi as Client

# Get BINANCE orderbook of BTCUSDT
msg = {"channel": "orderbook", "symbol": 'BTCUSDT', "venues": ["BINANCE"], "action": "sub"}
# Get BINANCE klines of BTCUSDT at 1m interval
# msg = {"channel": "kline_1m", "symbol": "BTCUSDT", "venues": ["BINANCE"], "action": "sub"}
client = Client()
client.connect(md=True)
client.send_msg(msg)
```
Create Order
```python
from apifiny.ac_websocket import ACSpotApi as Client

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
# api key/secret are required for trade endpoints
client = Client(venue="BINANCE")
client.connect(account_id, api_key_id, secret_key)
client.new_order(**params)
# client.close()
```

Please find `examples` folder to check for more endpoints.


## Contributing

Contributions are welcome.<br/>
If you've found a bug within this project, please open an issue to discuss what you would like to change.<br/>
If it's an issue with the API, please report any new issues at [apifiny-connector-python issues](https://github.com/Apifiny-IO/apifiny-connector-python/issues)