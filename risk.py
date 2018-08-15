#!/usr/bin/python
import httplib
import urllib
from websocket import create_connection
import ssl

from login import getToken

token = getToken('tester', '12345')

ws = create_connection('wss://144.76.140.147/api/risk?token=%s' % token, sslopt={'cert_reqs': ssl.CERT_NONE})

while True:
  result =  ws.recv()
  print 'Received: %s' % result

ws.close()
