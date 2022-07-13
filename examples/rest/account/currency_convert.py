#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   currency_convert.py
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

venue = "COINBASEPRO"


params = {
    "accountId": account_id,
    "venue": venue,
    "currency": "USDT",
    "amount": 100,
    "targetCurrency": "USDC"
}

client = Client(venue, api_key_id, secret_key)

try:
    response = client.currency_convert(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
