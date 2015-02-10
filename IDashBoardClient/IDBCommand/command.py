__author__ = 'daiyue'
import os, commands, time, threading, subprocess, platform, json
from IDBEntry.config import IDBClientConfig

class CommandManager:
    config = IDBClientConfig()

    def executeCMD(self, cmd):
        #the list of commands to execute
        pf = platform.system()
        print pf
        dic = self.config.getCommandDictionary(pf)
        lines = ""
        try:
            p = subprocess.Popen(dic[cmd], shell=True, stdout=subprocess.PIPE, stderr= subprocess.STDOUT)
            lines = ""
            for line in p.stdout.readlines():
                print line
                lines += line
        except Exception, e:
            print e
        return lines

    #execute Auto commands
    def executeAutoCMD(self):
        dic = {}
        for cmd in self.config.autoCommands:
            #list += "'"+ cmd + "':'" + self.executeCMD(cmd = cmd) + "',"
            dic[cmd] = self.executeCMD(cmd=cmd)
        #global t
        #t = threading.Timer(2, self.executeAutoCMD)
        #t.start()
        return dic