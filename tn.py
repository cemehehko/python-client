#!/usr/bin/python
import httplib
import urllib
from websocket import create_connection
import ssl

from login import getToken

token = getToken('tester', '12345')

ws = create_connection('wss://144.76.140.147/api/tn?symbol=BTC/USD&token=%s' % token, sslopt={'cert_reqs': ssl.CERT_NONE})

order = '{"name": "AddOrder", "header": {"clorder_id": "1"}, "symbol": "BTC/USD", \
         "dir": "Buy",  \
         "amount": 1, "price": 1600.00000000}'

print '%s' % order
ws.send(order)
cancel = '{"name": "CancelOrder", "header": {"clorder_id": "2"}, "symbol": "BTC/USD", \
          "dir": "Buy", \
          "orig_clorder_id": "1" }'

print '%s' % cancel
ws.send(cancel)

# First you get active orders
while True:
  result =  ws.recv()
  print 'Received: %s' % result

ws.close()
