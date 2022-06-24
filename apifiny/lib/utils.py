#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
# @File    :   utils.py
# @Author  :   liuke
# @Version :   1.0
# @Desc    :   None
'''


import datetime
import hashlib
import random
import time
from urllib.parse import unquote, urlencode

import jwt
import yaml

from apifiny.lib import apifiny_urls


def read_conf(file):
    with open(file, 'r') as f:
        conf = yaml.load(f.read(), Loader=yaml.FullLoader)
    return conf


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


def gen_signature(account_id, secret_key_id, secret_key, params_string=None) -> str:
    """Generate signature
    Args:
        account_id (str): account_id
        secret_key_id (str): api_key_id
        secret_key (str): api_key
        params_string (str, optional): parameter. Defaults to None.

    Returns:
        str: jwt signature
    """
    digest = None
    if params_string:
        digest = hashlib.sha256(params_string.encode()).hexdigest()
    millis = datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
    signature = jwt.encode({
        'accountId': account_id,
        'secretKeyId': secret_key_id,
        'digest': digest,
        'exp': millis,
    }, secret_key, algorithm='HS256')
    # return signature.decode("utf-8")
    return signature


def generate_orderid(account_id) -> str:
    """Generate orderid
    Args:
        account_id (str): account_id

    Returns:
        str: orderid
    """
    return account_id.split('-')[-1] + str(int(time.time() * 1000)) + str(random.randint(100, 999))


def rest_url_yaml(unified_url, venue):
    if unified_url:
        return "https://api.apifiny.com/ac/v2/APIFINY"
    else:
        venue = venue.upper()
        urls = read_conf("apifiny/conf/url.yaml").get("REST")
        return urls.get(venue, f"https://api.apifiny.com/ac/v2/{venue}")


def ws_url_yaml(venue):
    venue = venue.upper()
    urls = read_conf("apifiny/conf/url.yaml").get("WS")
    return urls.get(venue, f"wss://api.apifiny.com")


def rest_url(unified_url, venue):
    if unified_url:
        return "https://api.apifiny.com/ac/v2/APIFINY"
    else:
        venue = venue.upper()
        urls = apifiny_urls.urls.get("REST")
        return urls.get(venue, f"https://api.apifiny.com/ac/v2/{venue}")


def ws_url(venue="GBBO", trade=True):
    venue = venue.upper()
    urls = apifiny_urls.urls.get("WS")

    if trade:
        url = urls.get(venue, "wss://api.apifiny.com")
        url = f"{url}/ws/trading"
    else:
        url = urls.get(venue, "wss://api.apifiny.com")
        if "api.apifiny" in url:
            url = f"{url}/ac/ws/v2/{venue}/asset"
        else:
            url = f"{url}/ac/ws/v2/asset"
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
