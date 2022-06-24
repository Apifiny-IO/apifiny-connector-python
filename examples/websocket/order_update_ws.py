#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  update_order_ws.py
@Time    :  2022/06/24 10:59:20
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
# connect trading,order stream
client.connect(account_id, api_key_id, secret_key)
