from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from VirtualMachines.models import VirtualMachine
import time, datetime
from django.contrib.sessions.models import Session
import json

# Create your views here.


def VMState(request):
    if 'uuid' in request.POST and request.POST['uuid']:
        uuid = request.POST['uuid'].strip('\n')
        try:
            vm = VirtualMachine.objects.filter(uuid=uuid)
            if len(vm) == 0:
                return HttpResponse('error')
        except Exception, e:
            print e
            return HttpResponse('error')
    elif 'IPAddress' in request.POST and request.POST['IPAddress']:
        ip = request.POST['IPAddress'].split('\n')[0]
        try:
            vm = VirtualMachine.objects.filter(IPAddress=ip)
            if len(vm) == 0:
                return HttpResponse('error')
        except Exception, e:
            print e
            return HttpResponse('error')
    else:
        return HttpResponse('error')
    if 'stateInfo' in request.POST and request.POST['stateInfo']:
        stateInfo = request.POST['stateInfo']
        vm[0].stateInfo = stateInfo
        vm[0].lastConnectTime = datetime.datetime.now()
        info = eval(request.POST['stateInfo'])
        vm[0].updateInfo(info)
        vm[0].save()
        #encode = json.dumps(eval(request.POST['stateInfo']))
        #print encode["HostName"]
    t = datetime.datetime.now()
    s = Session.objects.filter(expire_date__gte = t)
    response = HttpResponse()
    if len(s) != 0:
        response["content"] = "someone"
    else:
        response.write("noone")
        response["content"] = "noone"#response['person'] = "noone"
    return response


def helloServer(request):
    if 'uuid' in request.POST and request.POST['uuid']:
        uuid = request.POST['uuid'].strip('\n')
        print datetime.datetime.now()
        try:
            vm = VirtualMachine.objects.filter(uuid=uuid)
            if len(vm) != 0:
                vm[0].lastConnectTime = datetime.datetime.now()
                vm[0].save()
            else:
                return
        except Exception, e:
            print e
    elif 'IPAddress' in request.POST and request.POST['IPAddress'] and 'Port' in request.POST and request.POST['Port']:
        ip = request.POST['IPAddress'].split('\n')[0]
        port = request.POST['Port']
        print datetime.datetime.now()
        try:
            vm = VirtualMachine.objects.filter(IPAddress=ip)
            if len(vm) != 0:
                vm[0].lastConnectTime = datetime.datetime.now()
                vm[0].port = port
                vm[0].save()
            else:
                return
        except Exception, e:
            print e
            return
    else:
        return
    #return HttpResponse(json.dumps({"haha":"Hello world"}))
    r = HttpResponse()
    r.write("hello world")
    r["content"] = "helloworld"
    #return HttpResponse("hello world")
    return r


def get_my_VMs(request):
    if request.user.is_authenticated():
        virtual_machines = VirtualMachine.objects.filter(vmUser=request.user, state__lt=3)
        myVMs = []
        for virtual_machine in virtual_machines:
            try:
                application = virtual_machine.vm.order_by('submissionTime').first()
                dic = {
                    "id": virtual_machine.id,
                    "uuid": virtual_machine.uuid,
                    "state": virtual_machine.state,
                    "parameter":
                    {
                        "os": application.OS,
                        "memory": application.Memory,
                        "hostname": virtual_machine.hostname,
                        "username": virtual_machine.username
                    },
                    "treatment": "edit/delete"
                }
            except Exception, e:
                print e
                dic = {

                }
            finally:
                myVMs.append(dic)
        response={'data': myVMs}
        response['Access-Control-Allow-Origin'] = '*'
        return HttpResponse(json.dumps(response))
    else:
        return render_to_response('index.html', locals())