__author__ = 'wcx'

import threading
import time
import socket
from VirtualMachines.models import VirtualMachine
from Applications.models import Application
import random


class NotifyThread(threading.Thread):
    application = None

    def run(self):
        if not self.application:
            return "no application error"
        print "start.... %s" % (self.getName(),)
        host = None
        if self.application.type == 0:
            hosts = VirtualMachine.objects.filter(uuid=None)
            host = random.sample(hosts, 1)[0]
            self.application.pvm=host
        else:
            host = self.application.pvm
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print host.IPAddress
            sock.connect((host.IPAddress, host.port))
            types = ['new', 'delete', 'start', 'shutdown', 'savestate']
            web_server_request = {"request_id": self.application.id, "request_type": types[self.application.type],
                                  "request_userid": self.application.applicant.id}
            if self.application.type == 0:  # create
                web_server_request['request_pwd']= self.application.pwd
            else:
                web_server_request['vm_name'] = self.application.vm.hostname
                web_server_request['vm_uuid'] = self.application.vm.uuid
            sock.send(str(web_server_request))

            recv_str = sock.recv(1024)
            #print recv_str
            recv_dict = eval(recv_str)
            if recv_dict['request_id'] != self.application.id:
                print "error"
            if recv_dict['request_response'] == 'received' and self.application.state == 1:
                self.application.state = 3
                print "doing"
            else:
                self.application.state = 5

        except Exception, e:
            self.application.state = 5
            print e
        finally:
            self.application.save()
            sock.close()
            print "end.... %s" % (self.getName(),)
