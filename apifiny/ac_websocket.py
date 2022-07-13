#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
====================================
@File    :  ac_websocket.py
@Time    :  2022/06/23 18:20:14
@Author  :  LiuKeCode@hotmail.com
@Desc    :  None
====================================
"""
# here put the import lib

import json
import ssl
import sys
import time
import traceback
from threading import Thread

import websocket

from .lib.utils import gen_signature, ws_url

# API Doc https://doc.apifiny.com/connect/#introduction

###################################################################################

class ACWebSocket(object):

    def __init__(self, venue, test=False):
        if venue:
            self.host = ws_url(venue, test)
        self.ws = None
        self.thread = None
        self.is_connected = None
        self.test = test

    def connect(self, md=False, trace=False):
        """
        :param md       : market data
        :param trace    : If websocket journal activities need to be tracked. Check StreamHandler for it.
        :return:
        """
        # Renew websocket API info
        if md:
            if self.test:
                self.host = "ws://sandbox.apifiny.com/md/ws/v1"
            else:
                self.host = "wss://api.apifiny.com/md/ws/v1"
        print(f"Connect url: {self.host}")
        # Websocket journal
        websocket.enableTrace(trace)
        self.ws = websocket.WebSocketApp(self.host,
                                         on_message=self.onMessage,
                                         on_error=self.onError,
                                         on_close=self.onClose,
                                         on_open=self.onOpen)
        sslopt = {"cert_reqs": ssl.CERT_NONE}
        self.thread = Thread(target=self.ws.run_forever, args=(None, sslopt))
        self.thread.start()

    def reconnect(self):
        # To close the previous session
        self.close()
        # To reconnect using the following para
        self.ws = websocket.WebSocketApp(self.host,
                                         on_message=self.onMessage,
                                         on_error=self.onError,
                                         on_close=self.onClose,
                                         on_open=self.onOpen)
        sslopt = {"cert_reqs": ssl.CERT_NONE}
        self.thread = Thread(target=self.ws.run_forever, args=(None, sslopt))
        self.thread.start()

    def close(self):
        if self.thread and self.thread.isAlive():
            # print("APIFINY.close")
            self.ws.close()
            self.thread.join()

    def onMessage(self, ws, evt):
        """信息推送"""
        print(f"APIFINY.recvMsg: {evt}")
        # evt = json.loads(evt)

    def onError(self, ws, evt):
        print("APIFINY.onError_API:{}".format(evt))

    def onClose(self, ws, *args):
        print("APIFINY.Websocket.onClose\n")

    def onOpen(self, ws):
        self.is_connected = 1
        print("APIFINY.Websocket.onOpen\n")
    # ----------------------------------------------------------------------

    def login(self, secret_key_id, secret_key):
        while not self.is_connected:
            pass
        timestamp = int(time.time() * 1000) - 500
        sign = gen_signature(secret_key, f"timestamp={timestamp}")
        auth = {"action":"auth","data":{"timestamp":timestamp,"apiKey":secret_key_id,"signature":sign}}
        print(auth)
        try:
            self.ws.send(json.dumps(auth))
        except websocket.WebSocketConnectionClosedException as ex:
            print("APIFINY.login Exception:{},{}".format(str(ex), traceback.format_exc()), file=sys.stderr)
        except Exception as ex:
            print("APIFINY.login Exception:{},{}".format(str(ex), traceback.format_exc()), file=sys.stderr)

    def send_msg(self, msg):
        while not self.is_connected:
            pass
        print("APIFINY.sendMsg: {}".format(msg))
        if isinstance(msg, dict):
            msg = json.dumps(msg)
        try:
            self.ws.send(msg)
        except websocket.WebSocketConnectionClosedException as ex:
            print("APIFINY.sendMsg Exception:{},{}".format(str(ex), traceback.format_exc()), file=sys.stderr)
        except Exception as ex:
            print("APIFINY.sendMsg Exception:{},{}".format(str(ex), traceback.format_exc()), file=sys.stderr)

    def send_heart_beat(self):
        """
        HeartBeat to maintain connection with the API
        """
        heart_beat_ping = {"action":"heartbeat","data":"ping"}
        try:
            print("APIFINY.sendHeartBeat")
            self.ws.send(json.dumps(heart_beat_ping))
        except websocket.WebSocketConnectionClosedException as ex:
            print("APIFINY.sendHeartBeat Exception:{}".format(str(ex)), file=sys.stderr)
    # ----------------------------------------------------------------------

########################################################################


class ACSpotApi(ACWebSocket):
    """AC Spot trade"""

    def __init__(self, venue=None, test=False):
        """Constructor"""
        super(ACSpotApi, self).__init__(venue, test)

    def new_order(self, **kwargs):
        """Create Order"""
        # print("APIFINY.NewOrder:{}".format(kwargs))
        msg = {"action": "newOrder","data": kwargs}
        self.send_msg(msg)

    def cancel_order(self, **kwargs):
        """Cancel Order"""
        # print("APIFINY.CancelOrder:{}".format(kwargs))
        msg = {"action": "cancelOrder","data": kwargs}
        self.send_msg(msg)

    def cancel_all_order(self, **kwargs):
        """Cancel All Order"""
        # print("APIFINY.CancelAllOrder:{}".format(kwargs))
        msg = {"action": "cancelAllOrder","data": kwargs}
        self.send_msg(msg)
