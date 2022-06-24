#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  cancel_all_order_ws.py
@Time    :  2022/06/24 10:55:19
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

from apifiny.ac_websocket import ACSpotApi as Client

account_id = ""
api_key_id = ""
secret_key = ""

venue = "GBBO"
symbol = "BTCUSDT"

params = {"venue": venue, "symbol": symbol}

client = Client(venue=venue)
client.connect(account_id, api_key_id, secret_key)
client.cancel_order(**params)
client.close()
