#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   query_account_history.py
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
    "startTimeDate": 1640966400000,
    "endTimeDate": 1641139200000,
    "page": '1',
    "limit": 100
}

client = Client(unified_url, venue, account_id, api_key_id, secret_key)

try:
    response = client.query_account_history(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
