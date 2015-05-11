__author__ = 'wcx'

import httplib, urllib, time
from command import *
import types

httpClient = None
t = None
headers = {"Content-type": "application/x-www-form-urlencoded" \
                    , "Accept": "text/html"}
#headers = {"Host":"192.168.199.220", "Accept": "text/plain"}

def sendCommandResult(api, params):
    serverHost = getServerHost()
    serverPort = getServerPort()
    response = None
    stateHttpClient = None
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
    response = None
    while(True):
        state = 1
        myip = executeCMD('inet4')
        uuid = executeCMD('uuid')
        params = urllib.urlencode({'IPAddress': myip, 'Port': 23333, 'uuid': uuid})
        response = sendCommandResult(api="/helloServer/", params=params)
        if response and response.status == 200:
            #execute command and send to server
            num = 0
            while(True):
                if(state == 1):
                    result = executeAutoCMD()
                    params = urllib.urlencode({"stateInfo": result, "IPAddress": myip, "uuid": uuid})
                    response = sendCommandResult(api="/saveVMState/", params=params)
                else:
                    params = urllib.urlencode({"IPAddress": myip})
                    response = sendCommandResult(api="/saveVMState/", params=params)
                if response and response.status == 200:
                    if "content" in response.msg.dict and response.msg.dict["content"] == "someone":
                        num = 0
                        state = 1
                    else:
                        state = 0
                        num += 1
                        if num == 10:
                            num = 0
                            state = 1
                    time.sleep(4)
                else:
                    state = 1
                    num = 0
                    break
        time.sleep(5000)
    return
