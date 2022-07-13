#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   query_algo_order_history.py
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


venue = "GBBO"

params = {
    "accountId": account_id,
    "limit": "100",
    "symbol": "BTCUSDT",
    "side": "BUY",
    "startTime": 1651334400000,
    "endTime": 1651420800000,
}

client = Client(venue, api_key_id, secret_key)

try:
    response = client.query_algo_order_history(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
