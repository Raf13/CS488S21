#!usr/bin/env python

from socket import *
import sys
import select
#import time
#import json

host = "0.0.0.0"
port = 9999 # int(sys.argv[1])
s = socket(AF_INET, SOCK_DRGM)
s.bind((host,port))

buf = ?
adder = (port,host)
#not complete...

while(data):
	#sys.stdin.read(buf)
	if(s.send(data,adder)):