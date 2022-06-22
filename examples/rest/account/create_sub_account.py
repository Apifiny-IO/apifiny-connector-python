#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   create_sub_account.py
# @Author  :   LiukeCode@hotmail.com
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
venue = "BITTREX"

params = {
    "accountId": account_id,
    "venue": venue
}

client = Client(unified_url, venue, account_id, api_key_id, secret_key)

try:
    response = client.create_sub_account(**params)
    logging.info(response)
except Exception as e:
    logging.error(e)
    raise
