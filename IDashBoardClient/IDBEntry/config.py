__author__ = 'daiyue'

class IDBClientConfig:
    autoCommands = ["HostName", "UserName", "CPUInfo", "Top"]
    commandMacDictionary = {'Top': "Top -l 1 -n 10", 'UName': "uname -a", 'HostName': "hostname", 'UserName': "whoami", 'CPUInfo':"sysctl -n machdep.cpu.brand_string"}
    commandLinuxDictionary = {'Top': "top -bn 1", 'UName': "uname -a", 'HostName': "hostname",'CPUInfo':'cat /proc/cpuinfo | grep name|cut -f2 -d:|uniq -c', 'UserName': "whoami"}
    commandWindowsDictionary = {}
    port = 8000

    def getCommandDictionary(self, pf):
        if pf == "Windows":
            return self.commandWindowsDictionary
        elif pf == "Linux":
            return self.commandLinuxDictionary
        elif pf == "Darwin":
            return self.commandMacDictionary

    @staticmethod
    def getServerHost():
        return "192.168.196.1"


    def getServerPort(self):
        return 8000

    def getSocketPort(self):
        return self.port
    def setSocketPort(self, p):
        self.port = p
        return