#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  rest_api.py
@Time    :  2022/07/13 14:43:51
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import json
import time

import requests

from .lib.utils import gen_signature, prepare_params, rest_url


class API:
    def __init__(self, venue="GBBO", key_id=None, secret=None, test=False, recv_window=None):
        self.secret_key_id = key_id
        self.secret_key = secret
        self.venue = venue
        self.test = test
        self.recv_window = recv_window
        self.session = requests.Session()

    def _http_request(self, method, path, params=None, unified_url=True):
        self.base_url = rest_url(unified_url, self.venue, self.test)
        url = self.base_url + path
        rep = None
        header = {}
        if method.lower() == 'get':
            if params:
                params["timestamp"] = int(time.time() * 1000)
                params["recvWindow"] = self.recv_window
                params_string = prepare_params(params)
                header["apiKey"] = self.secret_key_id
                header["signature"] = gen_signature(self.secret_key, params_string)
            rep = self.session.get(url, params=params, headers=header)

        if method.lower() == 'post':
            params["timestamp"] = int(time.time() * 1000)
            params["recvWindow"] = self.recv_window
            params_json_string = json.dumps(params)
            header["Content-Type"] = "application/json; charset=utf-8"
            header["apiKey"] = self.secret_key_id
            header["signature"] = gen_signature(self.secret_key, params_json_string)
            rep = self.session.post(url, data=params_json_string, headers=header)
        try:
            data = rep.json()
        except ValueError:
            data = rep.text
        return data

    # Base Information
    def server_time(self):
        return self._http_request("get", "/utils/currentTimeMillis", unified_url=False)

    # unified_url
    def list_venue(self):
        return self._http_request("get", "/utils/listVenueInfo")

    def list_currency(self):
        return self._http_request("get", f"/utils/listCurrency", unified_url=False)

    def list_symbol(self):
        return self._http_request("get", f"/utils/listSymbolInfo", unified_url=False)

    # Trading API
    def new_order(self, **kwargs):
        return self._http_request("post", "/order/newOrder", kwargs, unified_url=False)

    def cancel_order(self, **kwargs):
        return self._http_request("post", "/order/cancelOrder", kwargs, unified_url=False)

    def cancel_all_order(self, **kwargs):
        return self._http_request("post", "/order/cancelAccountVenueAllOrder", kwargs, unified_url=False)

    def query_order(self, **kwargs):
        return self._http_request("get", "/order/queryOrderInfo", kwargs, unified_url=False)

    # unified_url
    def query_multiple_orders(self, **kwargs):
        return self._http_request("get", "/order/listMultipleOrderInfo", kwargs)

    def query_open_orders(self, **kwargs):
        return self._http_request("get", "/order/listOpenOrder", kwargs, unified_url=False)

    # unified_url
    def query_completed_orders(self, **kwargs):
        return self._http_request("get", "/order/listCompletedOrder", kwargs)

    # unified_url
    def query_filled_orders(self, **kwargs):
        return self._http_request("get", "/order/listFilledOrder", kwargs)

    # SOR Trading API
    # unified_url
    def query_algo_order(self, **kwargs):
        return self._http_request("get", "/api/v2/algo/query-order-info", kwargs)

    # unified_url
    def query_algo_open_orders(self, **kwargs):
        return self._http_request("get", "/api/v2/algo/list-open-order", **kwargs)

    # unified_url
    def query_algo_order_detail(self, **kwargs):
        return self._http_request("get", "/api/v2/algo/order-detail", kwargs)

    # unified_url
    def query_algo_order_history(self, **kwargs):
        return self._http_request("get", "/api/v2/algo/list-order-history", kwargs)

    # Account API
    # unified_url
    def create_sub_account(self, **kwargs):
        return self._http_request("get", "/account/createSubAccount", kwargs)
        
    # unified_url
    def query_account_info(self, **kwargs):
        return self._http_request("get", "/account/queryAccountInfo", kwargs)

    def query_asset(self, **kwargs):
        return self._http_request("get", "/asset/listBalance", kwargs, unified_url=False)

    def query_trading_fee_rate(self, **kwargs):
        return self._http_request("get", "/asset/getCommissionRate", kwargs, unified_url=False)

    # unified_url
    def query_transaction_fee(self, **kwargs):
        return self._http_request("get", "/utils/query-transaction-fee", kwargs)

    # unified_url
    def deposit_address(self, **kwargs):
        return self._http_request("get", "/asset/queryAddress", kwargs)

    # unified_url
    def creat_withdraw_ticket(self, **kwargs):
        return self._http_request("get", "/asset/createWithdrawTicket", kwargs)

    # unified_url
    def withdraw(self, **kwargs):
        return self._http_request("post", "/asset/withdraw", kwargs)

    # unified_url
    def fiat_withdraw(self, **kwargs):
        return self._http_request("post", "/asset/fiat-withdraw", kwargs)

    # unified_url
    def query_instant_quota(self, **kwargs):
        return self._http_request("get", "/asset/query-max-instant-amount", kwargs)

    # unified_url
    def transfer(self, **kwargs):
        return self._http_request("post", "/asset/transferToVenue", kwargs)

    def currency_convert(self, **kwargs):
        return self._http_request("post", "/asset/currencyConversion", kwargs, unified_url=False)

    # unified_url
    def query_account_history(self, **kwargs):
        return self._http_request("get", "/asset/queryAssetActivityList", kwargs)
