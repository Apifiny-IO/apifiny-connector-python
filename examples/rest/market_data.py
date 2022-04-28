#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   market_data.py
# @Author  :   liuke
# @Version :   1.0
# @Desc    :   None
'''

import logging
from apifiny.rest_market import MarketData as Client
from apifiny.lib.utils import config_logging

config_logging(logging, logging.INFO)

venue = "BINANCE"
symbol = "BTCUSDT"

client = Client()

logging.info(client.cob(symbol))
# logging.info(client.market_order_book(venue, symbol))
# logging.info(client.market_ticker(venue, symbol))
# logging.info(client.market_trade(venue, symbol))
# logging.info(client.market_kline(venue, "BTC", "USDT", "1m"))
