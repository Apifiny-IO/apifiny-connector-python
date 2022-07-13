#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  demo_market_data.py
@Time    :  2022/07/13 14:45:25
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import logging

from apifiny.lib import venue_list
from apifiny.lib.utils import config_logging
from apifiny.rest_market import MarketData as Client

config_logging(logging, logging.INFO)

venue = venue_list.BINANCE
symbol = "BTCUSDT"

# test=True is sandbox env,default is prod env.
client = Client()


logging.info(client.cob(symbol))
logging.info(client.market_order_book(venue, symbol))
logging.info(client.market_ticker(venue, symbol))
logging.info(client.market_trade(venue, symbol))
logging.info(client.market_kline(venue, "BTC", "USDT", "1m"))
