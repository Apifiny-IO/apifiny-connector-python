#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   withdraw_crypto.py
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

ticket_params = {
    "accountId": account_id,
    "venue": venue
}

client = Client(unified_url, venue, account_id, api_key_id, secret_key)

try:
    ticket = client.creat_withdraw_ticket(**ticket_params)
    withdraw_params = {
        "accountId": account_id,
        "venue": venue,
        "coin": "USDT.TRON",
        "amount": 100,
        "address": "",
        "memo": "",
        "ticket": ticket
    }
    response = client.withdraw(**withdraw_params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
