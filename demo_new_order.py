#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  demo_new_order.py
@Time    :  2022/07/12 15:56:20
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import logging

from apifiny.lib import venue_list
from apifiny.lib.utils import config_logging, generate_orderid
from apifiny.rest_api import API as Client

config_logging(logging, logging.INFO)

account_id = "Replace with your account id"
api_key_id = "Replace with your api key"
secret_key = "Replace with your secret key"

# venue = "GBBO"
venue = venue_list.BINANCE

# LIMIT
params = {
    "accountId": account_id,
    "venue": venue,
    "orderId": generate_orderid(account_id),
    "orderInfo": {
        "limitPrice": "10000",
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

# test=True is sandbox env,default is prod env.
client = Client(venue, api_key_id, secret_key)

try:
    response = client.new_order(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
