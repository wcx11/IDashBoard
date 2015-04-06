__author__ = 'wcx'

from config import *
import subprocess, platform
def executeCMD(cmd):
    pf = platform.system()
    dic = getCommandDictionary(pf)
    lines = ""
    try:
        p = subprocess.Popen(dic[cmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            lines += line
    except Exception, e:
        print e
    finally:
        return lines

def executeAutoCMD():
    dic = {}
    for cmd in autoCommands:
        dic[cmd] = executeCMD(cmd=cmd)
    return dic