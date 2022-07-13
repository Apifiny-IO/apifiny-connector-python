#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  query_transaction_fee.py
@Time    :  2022/07/12 15:49:14
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import logging
from apifiny.rest_api import API as Client
from apifiny.lib.utils import config_logging

config_logging(logging, logging.INFO)

account_id = ""
api_key_id = ""
secret_key = ""


params = {
    "type": "withdraw",
    "currency": "USDT",
    "coin": "USDT.ETH",
    "from": "BINANCE",
    "to": "APIFINY",
}

client = Client()

try:
    response = client.query_transaction_fee(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
