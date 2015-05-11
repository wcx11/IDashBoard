from django.db import models
from django.contrib.auth.models import User
from VirtualMachines.models import VirtualMachine
# Create your models here.


class Application(models.Model):
    type = models.IntegerField()  # 0 = create, 1 = delete
    OS = models.IntegerField(null=True)
    HostName = models.TextField(null=True)
    UserName = models.TextField(null=True)
    pwd = models.TextField(null=True)
    Memory = models.IntegerField(null=True)  # 0 = 1024, 1 = 2048
    state = models.IntegerField()  # 0 = applied, 1 = passed, 2 = refused, 3 = doing, 4 = done, 5 = error
    submissionTime = models.DateTimeField(auto_now=True, auto_now_add=False)
    applicant = models.ForeignKey(User, null=False, related_name='applicant')
    reviewer = models.ForeignKey(User, null=True, related_name='reviewer')
    vm = models.ForeignKey(VirtualMachine, null=True, related_name='vm')
    pvm = models.ForeignKey(VirtualMachine, null=True, related_name='pvm')