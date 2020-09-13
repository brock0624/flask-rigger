# -*- coding: utf-8 -*- 
import socket
def gethostname():
    hostname = socket.gethostname()
    return hostname
def getip(hostname):
    ip = socket.gethostbyname(hostname)
    return ip