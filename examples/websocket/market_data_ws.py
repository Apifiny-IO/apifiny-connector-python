#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  market_data_ws.py
@Time    :  2022/06/24 11:18:57
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

from apifiny.ac_websocket import ACSpotApi as Client

msg = {"channel": "orderbook", "symbol": 'BTCUSDT', "venues": ["BINANCE"], "action": "sub"}

"""
# Conslidated Order Book Channel
{"channel": "cob", "symbol": "BTCUSDT", "action": "sub"}
# Order Book Channel
{"channel": "orderbook", "symbol": "BTCUSDT", "venues": ["BINANCE"], "action": "sub"}
# Ticker Channel
{"channel": "ticker", "symbol": "BTCUSDT", "venues": ["BINANCE"], "action": "sub"}
# Trades Channel
{"channel": "trade", "symbol": "BTCUSDT", "venues": ["BINANCE"], "action": "sub"}
# OHLCV Channel
{"channel": "kline_1m", "symbol": "BTCUSDT", "venues": ["BINANCE"], "action": "sub"}
"""

client = Client()
client.connect(md=True)
client.send_msg(msg)
