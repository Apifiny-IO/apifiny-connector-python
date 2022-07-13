#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  base_info.py
@Time    :  2022/07/12 15:48:18
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import logging
from apifiny.rest_api import API as Client
from apifiny.lib.utils import config_logging

config_logging(logging, logging.INFO)

venue = "GBBO"

client = Client(venue)

logging.info(client.server_time())
logging.info(client.list_venue())
logging.info(client.list_symbol())
logging.info(client.list_currency())
