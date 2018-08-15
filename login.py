#!/usr/bin/python
import requests
import simplejson
import requests

def getToken(login, password):
  requests.packages.urllib3.disable_warnings()
  headers = {"Content-Type":"application/json"}
  data = simplejson.dumps({"username": login, "password": password})
  response = requests.post("https://144.76.140.147/api/user/login",data=data, headers=headers, verify=False)

  logon = simplejson.loads(response.text)

  return logon['token']


print 'token: %s' % getToken('tester', '12345')
