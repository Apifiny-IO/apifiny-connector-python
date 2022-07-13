#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  market_data.py
@Time    :  2022/07/12 15:48:41
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

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
