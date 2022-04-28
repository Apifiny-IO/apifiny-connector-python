#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   query_filled_orders.py
# @Author  :   liuke
# @Version :   1.0
# @Desc    :   None
'''

import logging
from apifiny.rest_api import API as Client
from apifiny.lib.utils import config_logging

config_logging(logging, logging.INFO)

account_id = ""
api_key_id = ""
secret_key = ""

unified_url = True
venue = "GBBO"

params = {
    "accountId": account_id,
    "venue": venue,
    "orderId": "order_id",
    "symbol": "BTCUSDT",
    "limit": 100,
    "startTime": 1640966400000,
    "endTime": 1641139200000
}

client = Client(unified_url, venue, account_id, api_key_id, secret_key)

try:
    response = client.query_filled_orders(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
