#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  cancel_order_ws.py
@Time    :  2022/06/24 10:51:30
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

params = {"orderId": account_id, "venue": venue}

client = Client(venue=venue)
client.connect()
client.login(api_key_id, secret_key)
client.cancel_all_order(**params)
client.close()
