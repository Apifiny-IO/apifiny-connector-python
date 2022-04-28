#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   base_info.py
# @Author  :   liuke
# @Version :   1.0
# @Desc    :   None
'''

import logging
from apifiny.rest_api import API as Client
from apifiny.lib.utils import config_logging

config_logging(logging, logging.INFO)

unified_url = False
venue = "GBBO"

client = Client(unified_url, venue)

logging.info(client.server_time())
logging.info(client.list_venue())
logging.info(client.list_symbol())
logging.info(client.list_currency())
