#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  utils.py
@Time    :  2022/07/07 11:03:27
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import hashlib
import hmac
import random
import time
from urllib.parse import unquote, urlencode

from apifiny.lib import apifiny_urls


def clean_none_value(d) -> dict:
    out = {}
    for k in d.keys():
        if d[k] is not None:
            out[k] = d[k]
    return out


def encoded_string(query) -> str:
    return unquote(urlencode(query, True).replace("%40", "@"))


def prepare_params(params) -> str:
    return encoded_string(clean_none_value(params))


def gen_signature(secret_key, data) -> str:
    """Generate signature
    Args:
        secret_key (str): secret_key
        data (str): data
    Returns:
        str: hmac sha256 signature
    """
    message = data.encode("utf-8")
    return hmac.new(secret_key.encode("utf-8"), message, digestmod=hashlib.sha256).hexdigest()


def generate_orderid(account_id) -> str:
    """Generate orderid
    Args:
        account_id (str): account_id

    Returns:
        str: orderid
    """
    return "SDK_" + account_id.split('-')[-1] + str(int(time.time() * 1000)) + str(random.randint(100, 999))


def rest_url(unified_url, venue, test):
    if test:
        return f"http://api-sandbox.apifiny.com/ac/v2/{venue}"
    else:
        if unified_url:
            return "https://api.apifiny.com/ac/v2/APIFINY"
        else:
            venue = venue.upper()
            urls = apifiny_urls.urls.get("REST")
            return urls.get(venue, f"https://api.apifiny.com/ac/v2/{venue}")


def ws_url(venue="GBBO", test=False):
    venue = venue.upper()
    if test:
        url = f"ws://api-sandbox.apifiny.com/ws/stream"
    else:
        urls = apifiny_urls.urls.get("WS")
        url = urls.get(venue, "wss://api.apifiny.com")
        url = f"{url}/ws/stream"
    return url


def config_logging(logging, logging_level, log_file: str = None):
    logging.Formatter.converter = time.gmtime  # date time in GMT/UTC
    logging.basicConfig(
        level=logging_level,
        filename=log_file,
        format="%(asctime)s.%(msecs)03d UTC %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


if __name__ == '__main__':
    print(rest_url(False, "BINANCE"))
