from django.db import models

# Create your models here.
class VirtualMachine(models.Model):
    IPAddress = models.IPAddressField()
    port = models.PositiveIntegerField(null=True)
    state = models.IntegerField(null=True)#if the virtual machine is online
    lastConnectTime = models.DateTimeField(auto_now=True, auto_now_add=False)#when the client connect the server for the last time
    stateInfo = models.TextField()

