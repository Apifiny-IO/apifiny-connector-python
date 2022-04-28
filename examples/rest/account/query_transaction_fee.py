#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   query_transaction_fee.py
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

params = {
    "type": "withdraw",
    "currency": "USDT",
    "coin": "USDT.ETH",
    "from": "BINANCE",
    "to": "APIFINY",
}

client = Client(unified_url)

try:
    response = client.query_transaction_fee(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
