#!/usr/bin/python
from websocket import create_connection
import ssl
ws = create_connection("wss://144.76.140.147/api/tn?symbol=BTC%2FUSD&token=78e4daed-7f97-46d9-a87f-fc89adeaa8c3", sslopt={"cert_reqs": ssl.CERT_NONE})

while True:
  ws.recv()

order = '{"name": "AddOrder", "header": {"clorder_id": "1"}, "symbol": "BTC/USD", \
         "dir": "Buy",  \
         "amount": 1, "price": 1600.00000000,}'

print '%s' % order
ws.send(order)
cancel = '{"name": "CancelOrder", "header": {"clorder_id": "2"}, "symbol": "BTC/USD", \
          "dir": "Buy", \
          "orig_clorder_id": "1" }'

print '%s' % cancel
ws.send(cancel)

while True:
  result =  ws.recv()

print "Received '%s'" % result

ws.close()
