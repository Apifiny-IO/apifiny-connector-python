#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   rest_market.py
# @Author  :   liuke
# @Version :   1.0
# @Desc    :   None
'''

import requests


class MarketData:
    def __init__(self):
        self.base_url = "https://api.apifiny.com"
        self.session = requests.Session()

    def http_request(self, path):
        url = self.base_url + path
        rep = None
        rep = self.session.get(url)

        try:
            data = rep.json()
        except ValueError:
            data = rep.text
        return data

    # Market Data
    def cob(self, symbol):
        return self.http_request(f"/md/cob/v1/{symbol}")

    def market_order_book(self, venue, symbol):
        return self.http_request(f"/md/orderbook/v1/{symbol}/{venue}")

    def market_ticker(self, venue, symbol):
        return self.http_request(f"/md/ticker/v1/{symbol}/{venue}")

    def market_trade(self, venue, symbol):
        return self.http_request(f"/md/trade/v1/{symbol}/{venue}")

    def market_kline(self, venue, base, quote, period):
        return self.http_request(f"/md/kline/v1/{venue}/{base}/{quote}/{period}")
