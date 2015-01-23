__author__ = 'daiyue'
from IDBEntry.config import *
from IDBNetWork.connectServer import *
from IDBCommand.command import *
import threading, socket

def socketLoop():
    print("socketLoop")
    while True:
        listeningSock.accept()
        connection,addr = listeningSock.accept()
        print "a client have connected..."
        while True:
            try:
                connection.settimeout(5)
                buf = connection.recv(1024)
                if buf == "1":
                   connection.send("you have send me 1!welcome to server!")
                elif buf=="2":
                    connection.send("you have send me 2!I have recv!")
                elif buf=="3":
                    connection.send("close the connection!")
                    break
                else:
                   connection.send("unknow command!")
            except socket.timeout:
                print "time out"
        connection.close()
        print "a client exit..."
    return
def clientLoop():
    print "clientLoop"
    idbn.connectServer()

if __name__ == '__main__':
    #print "entry"
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 6000
    while True:
        try:
            listeningSock.bind(("127.0.0.1", port))
            idbn = IDBNetwork(port)
            idbn.config.setSocketPort(port)
            break;
        except Exception, e:
            print e
            port = port + 1
    listeningSock.listen(5)

    t1 = threading.Thread(target=socketLoop, name='socketLoopThread')
    t2 = threading.Thread(target=clientLoop, name='clientLoopThread')
    t1.start()
    t2.start()