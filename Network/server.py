#! /usr/bin/env python2

import socket

s = socket.socket()
host = socket.gethostname()
port = 1025
s.bind((host,port))

s.listen(5)
while True:
	c,addr = s.accept()
	print 'Got connection from', addr
	c.send('Thank you for connecting')
	c.close()
