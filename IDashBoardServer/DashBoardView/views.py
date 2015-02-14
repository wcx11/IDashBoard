from django.shortcuts import render, render_to_response
from django import template
from VirtualMachines.models import VirtualMachine
import datetime, time, json
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth



# Create your views here.

def HomePage(request):
    if request.user.is_authenticated():
        user = request.user
        ActiveVMs = getAllActiveVMs()
        #c = template.Context({'ActiveVMs':list})
        stateList = ['HostName', 'UserName', 'CPUInfo']
        #page = HomePage()
        return render_to_response('home.html', locals())
    else:
        return render_to_response('index.html', locals())

def home(request):
    return render_to_response('home.html')

def RefreshHomePage(request):
    if request.user.is_authenticated():
        ActiveVMs = getAllActiveVMs()
        response = {'ActiveVMs': ActiveVMs}
        response['Access-Control-Allow-Origin'] = '*'
        return HttpResponse(json.dumps(response))
    else:
        return render_to_response('index.html', locals())
def RefreshSimplePage(request):
    if request.user.is_authenticated():
        ActiveVMs = getAllActiveVMsSimple()
        response = {'ActiveVMs': ActiveVMs}
        response['Access-Control-Allow-Origin'] = '*'
        return HttpResponse(json.dumps(response))
    else:
        return render_to_response('index.html', locals())

def VMDetails(request, ip):
    vmDetail = {}
    try:
        vm = VirtualMachine.objects.filter(IPAddress=ip)
        if len(vm) != 0:
            vmDetail += {'IPAddress': vm[0].IPAddress, 'stateInfo': eval(vm[0].stateInfo)}
        else:
            vmDetail += {'IPAddress': [], 'stateInfo': []}
    except Exception, e:
        print e
        return
    return HttpResponse(json.dumps(vmDetail))

def getAllActiveVMsSimple():
    t = datetime.datetime.now()
    t -= datetime.timedelta(seconds=60)
    vms = VirtualMachine.objects.filter(lastConnectTime__gte = t)
    ActiveVMs = []
    for vm in vms:
        dic = {'IPAddress': vm.IPAddress, 'UserName': vm.username, 'HostName': vm.hostname, 'Memory': vm.mem}
        ActiveVMs.append(dic)
    return ActiveVMs

def getAllActiveVMs():
    t = datetime.datetime.now()
    t -= datetime.timedelta(seconds=60)
    vms = VirtualMachine.objects.filter(lastConnectTime__gte = t)
    ActiveVMs = []
    for vm in vms:
        dic = {'IPAddress': vm.IPAddress, 'stateInfo': eval(vm.stateInfo)}
        ActiveVMs.append(dic)
    return ActiveVMs

def login(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('username', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('password', ''):
            errors.append('Enter a message.')
        if not errors:
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")


