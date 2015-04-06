__author__ = 'wcx'

import httplib, urllib, time
from command import *
#from config import *

httpClient = None
t = None
headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/plain", "Host":"192.168.196.1"}

def sendCommandResult(api, params):
    serverHost = getServerHost()
    serverPort = getServerPort()
    response = None
    try:
        stateHttpClient = httplib.HTTPConnection(serverHost, serverPort, timeout = 30)
        stateHttpClient.request("POST", api, params, headers)
        response = stateHttpClient.getresponse()
    except Exception, e:
        print e
    finally:
        if(stateHttpClient):
            stateHttpClient.close()
        return response

def connectServer():
    while(True):
        params = urllib.urlencode({'IPAddress': '192.168.233.129', 'Port': 0})
        response = sendCommandResult(api = "/helloServer/", params = params)
        if response and response.status == 200:
            #execute command and send to server
            while(True):
                result = executeAutoCMD()
                params = urllib.urlencode({"stateInfo": result, "IPAddress": '192.168.233.129'})
                sendCommandResult(api = "/saveVMState/", params = params)
                time.sleep(3)
        else:
            time.sleep(5000)
    return
