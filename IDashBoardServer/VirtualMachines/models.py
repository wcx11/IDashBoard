from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class VirtualMachine(models.Model):
    uuid = models.TextField(null=True)
    vmUser = models.ForeignKey(User, related_name='vm_user', null=True)
    vmHost = models.ForeignKey('self', related_name='vm_host', null=True)
    IPAddress = models.TextField(null=True)
    port = models.PositiveIntegerField(null=True)
    state = models.IntegerField(null=True)  # 0 = online, 1 = offline, 2 = savestate, 3 = deleted
    lastConnectTime = models.DateTimeField(auto_now=True, auto_now_add=False)
    # when the client connect the server for the last time
    stateInfo = models.TextField(null=True)

    #from ifconfig command
    inet4 = models.TextField(null=True)
    bcast = models.TextField(null=True)
    inet6 = models.TextField(null=True)
    mask = models.TextField(null=True)
    DNS = models.TextField(null=True)

    #from top command
    users = models.TextField(null=True)
    loadAverage = models.TextField(null=True)
    tasks = models.TextField(null=True)
    percentCPU = models.TextField(null=True)
    mem = models.TextField(null=True)
    swap = models.TextField(null=True)
    process = models.TextField(null=True)
    #others
    hostname = models.TextField(null=True)
    username = models.TextField(null=True)
    cpuInfo = models.TextField(null=True)
    osInfo = models.TextField(null=True)


    def updateInfo(self, info):
        #infolist = ["HostName", "UserName", "CPUInfo",\
        #   "Tasks", "Memory", "percentCPU", "Swap",\
        #   "inet4", "bcast", "mask", "DNS", "inet6"]
        if "HostName" in info:
            self.hostname = info["HostName"]
        if "UserName" in info:
            self.username = info["UserName"]
        if "CPUInfo" in info:
            self.cpuInfo = info["CPUInfo"]
        if "Tasks" in info:
            self.tasks = info["Tasks"]
        if "Memory" in info:
            self.mem = info["Memory"]
        if "percentCPU" in info:
            self.percentCPU = info["percentCPU"]
        if "Swap" in info:
            self.swap = info["Swap"]
        if "inet4" in info:
            self.inet4 = info["inet4"]
        if "bcast" in info:
            self.bcast = info["bcast"]
        if "mask" in info:
            self.mask = info["mask"]
        if "DNS" in info:
            self.DNS = info["DNS"]
        if "inet6" in info:
            self.inet6 = info["inet6"]
        if "os" in info:
            self.osInfo = info["os"]
        if "process" in info:
            self.process = info["process"]