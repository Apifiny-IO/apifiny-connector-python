#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   rest_api.py
# @Author  :   liuke
# @Version :   1.0
# @Desc    :   None
'''

import json

import requests

from .lib.utils import gen_signature, prepare_params, rest_url


class API:
    def __init__(self, unified_url=True, venue="GBBO", account_id=None, key=None, secret=None, test=False):
        self.secret_key_id = key
        self.secret_key = secret
        self.account_id = account_id
        self.base_url = rest_url(unified_url, venue, test)
        self.session = requests.Session()

    def http_request(self, method, path, params=None):
        url = self.base_url + path
        rep = None
        if method.lower() == 'get':
            header = None
            if params:
                params_string = prepare_params(params)
                header = {'signature': gen_signature(
                    self.account_id, self.secret_key_id, self.secret_key, params_string)}
            rep = self.session.get(url, params=params, headers=header)

        if method.lower() == 'post':
            params_json_string = json.dumps(params)
            header = {'Content-Type': 'application/json; charset=utf-8',
                      'signature': gen_signature(self.account_id, self.secret_key_id, self.secret_key, params_json_string)}
            rep = self.session.post(
                url, data=params_json_string, headers=header)
        try:
            data = rep.json()
        except ValueError:
            data = rep.text
        return data

    # Base Information
    def server_time(self):
        return self.http_request("get", "/utils/currentTimeMillis")

    # unified_url
    def list_venue(self):
        return self.http_request("get", "/utils/listVenueInfo")

    # unified_url
    def list_currency(self):
        return self.http_request("get", f"/utils/listCurrency")

    # unified_url
    def list_symbol(self):
        return self.http_request("get", f"/utils/listSymbolInfo")

    # Trading API
    def new_order(self, **kwargs):
        return self.http_request("post", "/order/newOrder", kwargs)

    def cancel_order(self, **kwargs):
        return self.http_request("post", "/order/cancelOrder", kwargs)

    def cancel_all_order(self, **kwargs):
        return self.http_request("post", "/order/cancelAccountVenueAllOrder", kwargs)

    def query_order(self, **kwargs):
        return self.http_request("get", "/order/queryOrderInfo", kwargs)

    # unified_url
    def query_multiple_orders(self, **kwargs):
        return self.http_request("get", "/order/listMultipleOrderInfo", kwargs)

    def query_open_orders(self):
        return self.http_request("get", "/order/listOpenOrder", {
            "accountId": self.account_id,
        })

    # unified_url
    def query_completed_orders(self, **kwargs):
        return self.http_request("get", "/order/listCompletedOrder", kwargs)

    # unified_url
    def query_filled_orders(self, **kwargs):
        return self.http_request("get", "/order/listFilledOrder", kwargs)

    # SOR Trading API
    # unified_url
    def query_algo_order(self, **kwargs):
        return self.http_request("get", "/api/v2/algo/query-order-info", kwargs)

    # unified_url
    def query_algo_open_orders(self):
        return self.http_request("get", "/api/v2/algo/list-open-order", {
            "accountId": self.account_id,
        })

    # unified_url
    def query_algo_order_detail(self, **kwargs):
        return self.http_request("get", "/api/v2/algo/order-detail", kwargs)

    # unified_url
    def query_algo_order_history(self, **kwargs):
        return self.http_request("get", "/api/v2/algo/list-order-history", kwargs)

    # Account API
    # unified_url
    def create_sub_account(self, **kwargs):
        return self.http_request("get", "/account/createSubAccount", kwargs)
        
    # unified_url
    def query_account_info(self, **kwargs):
        return self.http_request("get", "/account/queryAccountInfo", kwargs)

    def query_asset(self, **kwargs):
        return self.http_request("get", "/asset/listBalance", kwargs)

    def query_trading_fee_rate(self, **kwargs):
        return self.http_request("get", "/asset/getCommissionRate", kwargs)

    # unified_url
    def query_transaction_fee(self, **kwargs):
        return self.http_request("get", "/utils/query-transaction-fee", kwargs)

    # unified_url
    def deposit_address(self, **kwargs):
        return self.http_request("get", "/asset/queryAddress", kwargs)

    # unified_url
    def creat_withdraw_ticket(self, **kwargs):
        return self.http_request("get", "/asset/createWithdrawTicket", kwargs)

    # unified_url
    def withdraw(self, **kwargs):
        return self.http_request("post", "/asset/withdraw", kwargs)

    # unified_url
    def fiat_withdraw(self, **kwargs):
        return self.http_request("post", "/asset/fiat-withdraw", kwargs)

    # unified_url
    def query_instant_quota(self, **kwargs):
        return self.http_request("get", "/asset/query-max-instant-amount", kwargs)

    # unified_url
    def transfer(self, **kwargs):
        return self.http_request("post", "/asset/transferToVenue", kwargs)

    def currency_convert(self, **kwargs):
        return self.http_request("post", "/asset/currencyConversion", kwargs)

    # unified_url
    def query_account_history(self, **kwargs):
        return self.http_request("get", "/asset/queryAssetActivityList", kwargs)
