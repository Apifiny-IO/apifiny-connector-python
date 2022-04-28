#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   deposit_address.py
# @Author  :   liuke
# @Version :   1.0
# @Desc    :   None
'''

'''
Allocate the funds to the target exchange sub-account after funds arrived at Apifiny. 
There is 0 fee for you to allocate to sub-account, using examples/funds_transfer.py.
'''


import logging
from apifiny.rest_api import API as Client
from apifiny.lib.utils import config_logging
config_logging(logging, logging.INFO)

account_id = "Replace with your account id"
api_key_id = "Replace with your api key"
secret_key = "Replace with your secret key"

unified_url = True
venue = "GBBO"


params = {
    "accountId": account_id,
    "venue": venue,
    "coin": "USDT.TRON",
}

client = Client(unified_url, venue, account_id, api_key_id, secret_key)

try:
    response = client.deposit_address(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
