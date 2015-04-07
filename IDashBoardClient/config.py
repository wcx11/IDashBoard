__author__ = 'wcx'

autoCommands = ["HostName", "UserName", "CPUInfo",\
                    "Tasks", "Memory", "percentCPU", "Swap",\
                    "inet4", "bcast", "mask", "DNS", "inet6", "os", "process"]
commandMacDictionary = {}
commandWindowsDictionary = {}
commandLinuxDictionary = {'Top': "top -bn 1 | head -n 5",\
                              'UName': "uname -a",\
                              'HostName': "hostname",\
                              'CPUInfo':'cat /proc/cpuinfo | grep name|cut -f2 -d:|uniq -c',\
                              'UserName': "whoami",\
                              'Tasks':'top -bn 1 | head -n 5 | grep -i "Tasks.*total.*running" | awk \'{print $2" "$4" "$6" "$8" "$10}\'',\
                              'Memory':'top -bn 1 | head -n 5 | grep -i "mem.*total.*used" | awk \'{print $3" "$5" "$7" "$9}\'',\
                              'percentCPU':'top -bn 1 | head -n 5 | grep -i "CPU.*us.*sy" | awk \'{print $2" "$4" "$6" "$8" "$10" "$12" "$14}\'',\
                              'Swap':'top -bn 1 | head -n 5 | grep -i "Swap.*total.*used" | awk \'{print $3" "$5" "$7" "$9}\'',\
                              'inet4':'ifconfig -a | grep -i  ^eth -A 3 | grep -i -o "inet addr:[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}" | awk -F ":" \'{print $2}\'',\
                              'bcast':'ifconfig -a | grep -i  ^eth -A 3 | grep -i -o "Bcast:[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}" | awk -F ":" \'{print $2}\'',\
                              'mask':'ifconfig -a | grep -i  ^eth -A 3 | grep -i -o "Mask:[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}.[0-9]\{1,3\}" | awk -F ":" \'{print $2}\'',\
                              'inet6':'ifconfig -a | grep -i  ^eth -A 3 | grep -i "inet6 addr:" | awk \'{print $3}\'',\
                              "DNS":'cat /etc/resolv.conf | grep nameserver | awk \'{print $2}\'',\
                              "os":'cat /etc/issue',\
			                'process':'top -bn 1 | grep -A 15 "PID" | sed "1 d"'}

def getCommandDictionary(pf):
    if pf == "Windows":
        return commandWindowsDictionary
    elif pf == "Linux":
        return commandLinuxDictionary
    elif pf == "Darwin":
        return commandMacDictionary

def getServerHost():
    return "127.0.0.1"

def getServerPort():
    return 8000
