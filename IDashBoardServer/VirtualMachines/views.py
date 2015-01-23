from django.shortcuts import render
from django.http import HttpResponse
from VirtualMachines.models import VirtualMachine
import time, datetime
import json

# Create your views here.

def VMState(request):
    if 'IPAddress' in request.POST and request.POST['IPAddress']:
        ip = request.POST['IPAddress']
        try:
            vm = VirtualMachine.objects.filter(IPAddress= ip)
            if len(vm) == 0:
                return
        except:
            return
    if 'stateInfo' in request.POST and request.POST['stateInfo']:
        stateInfo = request.POST['stateInfo']
        vm[0].stateInfo = stateInfo
        vm[0].lastConnectTime = datetime.datetime.now()
        vm[0].save()
        #b = eval(request.POST['stateInfo'])['HostName']
        #encode = json.dumps(eval(request.POST['stateInfo']))
        #print encode["HostName"]

    try:
        VirtualMachine.objects.filter()
    except:
        return HttpResponse("error")
    return HttpResponse("saveDone")

def helloServer(request):
    if 'IPAddress' in request.POST and request.POST['IPAddress'] and 'Port' in request.POST and request.POST['Port']:
        ip = request.POST['IPAddress']
        port = request.POST['Port']
        print datetime.datetime.now()
        try:
            vm = VirtualMachine.objects.filter(IPAddress= ip)
            if len(vm) != 0:
                vm[0].lastConnectTime = datetime.datetime.now()
                vm[0].port = port
                vm[0].save()
            else:
                newVM = VirtualMachine(IPAddress= ip, port= port, lastConnectTime = datetime.datetime.now())
                newVM.save()
        except Exception, e:
            print e
            return

    else:
        return
    return HttpResponse("Hello world")
