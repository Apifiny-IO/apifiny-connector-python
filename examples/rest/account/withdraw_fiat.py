#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   withdraw_fiat.py
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

ticket_params = {
    "accountId": account_id,
    "venue": "GBBO"
}
fiat_info = {
    "routingNumber": "",
    "code": "",
    "bankName": "",
                "bankAddress": "",
                "country": "",
                "beneficiaryName": "",
                "beneficiaryNumber": "",
                "emailAddress": "",
                "phoneNumber": ""
}
client = Client(unified_url, account_id=account_id, key=api_key_id, secret=secret_key)

try:
    ticket = client.creat_withdraw_ticket(**ticket_params)
    withdraw_params = {
        "accountId": account_id,
        "venue": "GBBO",
        "coin": "USD",
        "amount": 100,
        "ticket": ticket,
        "fiatInfo": fiat_info
    }
    response = client.fiat_withdraw(**withdraw_params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
