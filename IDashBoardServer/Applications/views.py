from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from Applications.models import Application
from VirtualMachines.models import VirtualMachine
import datetime, json
import random
from notifyThead import NotifyThread
# Create your views here.


def do_apply(request):
    errors = []
    if request.user.is_authenticated():
        if request.method == 'POST':
            if not request.POST.get('vm_type', ''):
                errors.append('select vm_type')
            if not request.POST.get('os', ''):
                errors.append('select os')
            if not request.POST.get('password', ''):
                errors.append('Enter a password.')
            if not request.POST.get('memory', ''):
                errors.append('select memory')
            if not errors:
                password = request.POST.get('password', '')
                try:
                    os = int(request.POST.get('os', ''))
                    memory = int(request.POST.get('memory', ''))
                    vm_type = int(request.POST.get('vm_type', ''))
                    new_application = Application(type=0, vm_type=vm_type, OS=os, pwd=password, Memory=memory,\
                                                  state=0, applicant=request.user, submissionTime=datetime.datetime.now())
                    new_application.save()
                except Exception, e:
                    print(e)
            else:
                return HttpResponseRedirect('/apply/')
            return HttpResponseRedirect('/applications/')
    else:
        return render_to_response('index.html', locals())


def delete_apply(request):
    errors = []
    if request.user.is_authenticated():
        if request.method == 'POST':
            if not request.body:
                errors.append('no id')
            if not errors:
                try:
                    virtualmachine = VirtualMachine.objects.get(id=int(eval(request.body)['id']))
                    new_application = Application(type=1, state=0, vm=virtualmachine, pvm=virtualmachine.vmHost,
                                                  applicant=request.user, submissionTime=datetime.datetime.now())
                    new_application.save()
                except Exception, e:
                    print(e)
            else:
                return HttpResponseRedirect('/apply/')
            return HttpResponseRedirect('/applications/')
    else:
        return render_to_response('index.html', locals())


def start_apply(request):
    errors = []
    if request.user.is_authenticated():
        if request.method == 'POST':
            if not request.body:
                errors.append('no id')
            if not errors:
                try:
                    virtualmachine = VirtualMachine.objects.get(id=int(eval(request.body)['id']))
                    new_application = Application(type=2, state=1, vm=virtualmachine, pvm=virtualmachine.vmHost,
                                                  applicant=request.user, submissionTime=datetime.datetime.now())

                    new_application.reviewer = request.user
                    new_application.save()
                    notify = NotifyThread()
                    notify.application = new_application
                    notify.start()
                except Exception, e:
                    print(e)
            else:
                return HttpResponseRedirect('/apply/')
            return HttpResponseRedirect('/applications/')
    else:
        return render_to_response('index.html', locals())


def stop_apply(request):
    errors = []
    if request.user.is_authenticated():
        if request.method == 'POST':
            if not request.body:
                errors.append('no id')
            if not errors:
                try:
                    virtualmachine = VirtualMachine.objects.get(id=int(eval(request.body)['id']))
                    new_application = Application(type=3, state=1, vm=virtualmachine, pvm=virtualmachine.vmHost,
                                                  applicant=request.user, submissionTime=datetime.datetime.now())

                    new_application.reviewer = request.user
                    new_application.save()
                    notify = NotifyThread()
                    notify.application = new_application
                    notify.start()
                except Exception, e:
                    print(e)
            else:
                return HttpResponseRedirect('/apply/')
            return HttpResponseRedirect('/applications/')
    else:
        return render_to_response('index.html', locals())

def savestate_apply(request):
    errors = []
    if request.user.is_authenticated():
        if request.method == 'POST':
            if not request.body:
                errors.append('no id')
            if not errors:
                try:
                    virtualmachine = VirtualMachine.objects.get(id=int(eval(request.body)['id']))
                    new_application = Application(type=4, state=1, vm=virtualmachine, pvm=virtualmachine.vmHost,
                                                  applicant=request.user, submissionTime=datetime.datetime.now())

                    new_application.reviewer = request.user
                    new_application.save()
                    notify = NotifyThread()
                    notify.application = new_application
                    notify.start()
                except Exception, e:
                    print(e)
            else:
                return HttpResponseRedirect('/apply/')
            return HttpResponseRedirect('/applications/')
    else:
        return render_to_response('index.html', locals())

def get_my_applications(request):
    if request.user.is_authenticated():
        applications = request.user.applicant.all()
        my_applications = []
        types = ["new", "delete", "start", "shutdown", "savestate"]
        for application in applications:
            try:
                dic = {
                    "id": application.id,
                    "type": types[application.type],
                    "applicant": application.applicant.username,
                    "parameter":
                    {
                        "os": application.OS,
                        "memory": application.Memory,
                        "vm_type": application.vm_type,
                        "hostname": application.HostName,
                        "username": application.UserName
                    },
                    "submissionTime": application.submissionTime.strftime("%Y-%m-%d-%H"),
                    "state": application.state
                }
                if application.vm:
                    dic["parameter"]["uuid"] = application.vm.uuid
            except Exception, e:
                print e
                dic = {

                }
            finally:
                my_applications.append(dic)
        response={'data': my_applications}
        response['Access-Control-Allow-Origin'] = '*'
        return HttpResponse(json.dumps(response))
    else:
        return render_to_response('index.html', locals())


def get_untreated_applications(request):
    if request.user.is_authenticated():
        applications = Application.objects.filter(state=0)
        untreated_applications = []
        typeset = ["new", "delete", "start", "shutdown", "savestate"]
        osset = ["Ubuntu 14.04 LTS",""]
        memoryset = ["1024M", "2048M"]
        for application in applications:
            try:
                dic = {
                    "id": application.id,
                    "type": typeset[application.type],
                    "applicant": application.applicant.username,
                    "parameter":
                    {
                        "os": osset[application.OS - 1],
                        "memory": memoryset[application.Memory - 1],
                        "hostname": application.HostName,
                        "username": application.UserName
                    },
                    "submissionTime": application.submissionTime.strftime("%Y-%m-%d-%H"),
                    "treatment": "accept/refuse"
                }
                if application.vm:
                    dic["parameter"]["uuid"] = application.vm.uuid
            except Exception, e:
                print e
                dic = {
                    "id": application.id,
                    "type": typeset[application.type],
                    "applicant": application.applicant.username,
                    "parameter":
                    {
                        "hostname": application.HostName,
                        "username": application.UserName
                    },
                    "submissionTime": application.submissionTime.strftime("%Y-%m-%d-%H"),
                    "treatment": "accept/refuse"
                }
                if application.vm:
                    dic["parameter"]["uuid"] = application.vm.uuid
            finally:
                untreated_applications.append(dic)
        response={'data': untreated_applications}
        response['Access-Control-Allow-Origin'] = '*'
        return HttpResponse(json.dumps(response))
    else:
        return render_to_response('index.html', locals())


def ratify_application(request):
    if not request.POST.get("id"):
        return HttpResponse("error")
    try:
        id = int(request.POST.get("id"))
        application = Application.objects.get(id=id)
        if application.state == 0:
            host = None
            vms = application.applicant.vm_user.filter(state__lt=4)
            if len(vms) == 0:
                hosts = VirtualMachine.objects.filter(uuid=None)
                host = random.sample(hosts, 1)[0]
                application.pvm=host
            else:
                host = vms[0].vmHost
            application.pvm = host
            application.state = 1
            application.reviewer = request.user
            application.save()
            notify = NotifyThread()
            notify.application = application
            notify.start()
        else:
            return HttpResponse("already treated")
    except Exception, e:
        print e
        return HttpResponse("error")
    return HttpResponse("ratified")


def ratify_all(request):
    if request.method == 'POST':
        try:
            applications = Application.objects.filter(state=0)
            for application in applications:
                application.state = 1
                application.reviewer = request.user
                application.save()
                notify = NotifyThread()
                notify.application = application
                notify.start()
        except Exception, e:
            print e
        return HttpResponse('ratified_all')


def refuse_all(request):
    if request.method == 'POST':
        try:
            applications = Application.objects.filter(state=0)
            for application in applications:
                application.state = 2
                application.reviewer = request.user
                application.save()
        except Exception, e:
            print e
    return HttpResponse('refuse_all')


def refuse_application(request):
    if not request.POST.get("id"):
        return HttpResponse("error")
    try:
        id = int(request.POST.get("id"))
        application = Application.objects.get(id=id)
        if application.state == 0:
            application.state = 2
            application.save()
        else:
            return HttpResponse("already treated")
    except Exception, e:
        print e
        return HttpResponse("error")
    return HttpResponse("refused")


def vmHost_reply(request):
    webServer_response = {}
    if 'request_id' in request.POST and request.POST['request_id']:
        application_id = request.POST['request_id']
        webServer_response['request_id'] = application_id
    else:
        webServer_response['request_response'] = "no request_id error"
        return HttpResponse(str(webServer_response))
    try:
        application = Application.objects.get(id=application_id)
        if 'error_information' in request.POST:
            application.state = 5
            application.save()
        else:
            webServer_response['request_type'] = request.POST['request_type']
            vm_uuid = request.POST['vm_uuid']
            if request.POST['request_type'] == 'new':
                vm_name = request.POST['vm_name']
                vm_username = request.POST['vm_username']
                vm = VirtualMachine.objects.filter(uuid=vm_uuid)
                if len(vm)!= 0:
                    webServer_response['request_response'] = "repeated uuid error"
                    return HttpResponse(str(webServer_response))
                newVM = VirtualMachine(uuid=vm_uuid, lastConnectTime=datetime.datetime.now(),
                                       hostname=vm_name, username=vm_username, state=1)
                newVM.vmHost = application.pvm
                newVM.vmUser = application.applicant
                newVM.save()
                application.vm = newVM
                application.state = 4

            elif request.POST['request_type'] == 'start':
                vm_ip = request.POST['vm_ip']
                vm = VirtualMachine.objects.get(uuid=vm_uuid)
                vm.IPAddress = vm_ip

                if vm.state < 3:
                    vm.state = 0
                    application.state = 4
                    vm.save()
            elif request.POST['request_type'] == 'shutdown':
                vm = VirtualMachine.objects.get(uuid=vm_uuid)
                if vm.state < 3:
                    vm.state = 1
                    application.state = 4;
                    vm.save()
                else:
                    application.state = 5
            elif request.POST['request_type'] == 'savestate':
                vm = VirtualMachine.objects.get(uuid=vm_uuid)
                if vm.state < 3:
                    vm.state = 2
                    application.state = 4;
                    vm.save()
                else:
                    application.state = 5
            elif request.POST['request_type'] == 'delete':
                vm = VirtualMachine.objects.get(uuid=vm_uuid)
                if vm.state < 3:
                    vm.state = 3
                    application.state = 4;
                    vm.save()
                else:
                    application.state = 5
        webServer_response['request_userid'] = request.POST['request_userid']
        webServer_response['request_response'] = "received"
    except Exception, e:
        print e
        application.state = 5
        webServer_response['request_response'] = str(e)
    finally:
        application.save()
        return HttpResponse(str(webServer_response))
