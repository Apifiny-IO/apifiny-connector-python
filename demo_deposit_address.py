#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  demo_deposit_address.py
@Time    :  2022/07/12 15:54:33
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

'''
Allocate the funds to the target exchange sub-account after funds arrived at Apifiny. 
There is 0 fee for you to allocate to sub-account, using examples/funds_transfer.py.
'''

import logging

from apifiny.lib import venue_list
from apifiny.lib.utils import config_logging
from apifiny.rest_api import API as Client

config_logging(logging, logging.INFO)

account_id = "Replace with your account id"
api_key_id = "Replace with your api key"
secret_key = "Replace with your secret key"

venue = venue_list.BINANCE


params = {
    "accountId": account_id,
    "venue": venue,
    "coin": "USDT.TRON",
}

client = Client(venue, api_key_id, secret_key)

try:
    response = client.deposit_address(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
