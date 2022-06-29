#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  new_order_ws.py
@Time    :  2022/06/24 10:46:12
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

from apifiny.ac_websocket import ACSpotApi as Client
from apifiny.lib import venue_list
from apifiny.lib.utils import generate_orderid

account_id = ""
api_key_id = ""
secret_key = ""

# venue = "GBBO"
venue = venue_list.BINANCE

# LIMIT
params = {
    "accountId": account_id,
    "venue": venue,
    "orderId": generate_orderid(account_id),
    "orderInfo": {
        "limitPrice": "30000",
        "orderSide": "BUY",
        "orderType": "LIMIT",
        "quantity": "0.0001",
        "symbol": "BTCUSDT",
        "timeInForce": 1,
    }
}
# MARKET BUY
# "orderInfo": {"orderSide": "BUY", "orderType": "MARKET", "symbol": "BTCUSDT", "total": "xx"}
# MARKET SELL
# "orderInfo": {"orderSide": "SELL", "orderType": "MARKET", "symbol": "BTCUSDT", "quantity": "xx"}
# STOP stopType = LOSS or ENTRY
# "orderInfo": {"limitPrice": "xx", "orderSide": "BUY", "orderType": "STOP",  "quantity": "xx", "symbol": "BTCUSDT",
#               "timeInForce": 1, "stopType": "LOSS", "triggerPrice": "xx"}
# SOR: venue = "GBBO"
# "orderInfo": {"limitPrice": "xx", "orderSide": "BUY", "orderType": "SOR",  "quantity": "xx", "symbol": "BTCUSDT", "timeInForce": 1}

client = Client(venue=venue)
client.connect(account_id, api_key_id, secret_key)
client.new_order(**params)
client.close()
