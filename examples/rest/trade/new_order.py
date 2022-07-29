#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   new_order.py
# @Author  :   liuke
# @Version :   1.0
# @Desc    :   None
'''

import logging
from apifiny.rest_api import API as Client
from apifiny.lib.utils import config_logging
from apifiny.lib.utils import generate_orderid

config_logging(logging, logging.INFO)

account_id = ""
api_key_id = ""
secret_key = ""

venue = "GBBO"

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
# SOR: unified_url = True
# "orderInfo": {"limitPrice": "xx", "orderSide": "BUY", "orderType": "SOR",  "quantity": "xx", "symbol": "BTCUSDT", "timeInForce": 1}
# ICEBERG
# "orderInfo": {"limitPrice": "xx", "orderSide": "BUY", "orderType": "ICEBERG",  "quantity": "0.1", "symbol": "BTCUSDT", 
# "timeInForce": 1, "average": 0.01, "variance": 0}

client = Client(venue, api_key_id, secret_key)

try:
    response = client.new_order(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
