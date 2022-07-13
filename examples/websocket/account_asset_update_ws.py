#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  account_update_ws.py
@Time    :  2022/06/24 11:03:31
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

client = Client(venue=venue)
# order/asset stream
client.connect()
client.login(api_key_id, secret_key)
