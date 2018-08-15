#!/usr/bin/python

import websocket
import thread
import time
import json
import logging
import signal
import datetime
import ssl

logging.basicConfig(filename='ticks.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def unsubscribe(*agrs):
    print "unsubcribe"
    unsubscribe = '{"name": "unsubscribe", \
                   "topic_id": "1" }'
    ws.send(unsubscribe)

def on_message(ws, message):
    print '%s: %s' % (datetime.datetime.now(), message)
    data = json.loads(message)
    if data['name']=='login_ack':

      # channel: "l1", "l2" or "trades"
      subscribe = '{"name": "subscribe", \
                   "channel": "l1", \
                   "symbols": ["BTC/USD"], \
                   "mode": "SnapshotAndOnline"}'
      ws.send(subscribe)
      signal.signal(signal.SIGINT, unsubscribe)

def on_error(ws, error):
    print error

def on_close(ws):
    unsubscribe = '{"name": "unsubscribe", \
                   "topic_id": "1" }'
    ws.send(unsubscribe)
    print "closed"

def on_open(ws):
  login = '{"name": "login", \
            "user_id": "anonymous", \
            "token": "", \
            "ver": "1"}'
  ws.send(login)

host = "wss://144.76.140.147/api/md"
ws = websocket.WebSocketApp(host,
                         on_message=on_message,
                         on_error=on_error,
                         on_close=on_close)
ws.on_open=on_open
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
