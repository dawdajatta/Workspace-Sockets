#!/usr/bin/env python

"""
A simple echo client
"""

import socket
import sys

host = '67.20.210.20'
port = 3000
size = 512

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to the port where the server is listening
server_address = (host, port)
print >>sys.stderr, 'Connecting to %s port %s' % server_address
sock.connect(server_address)

try:
	#Send data
	message = 'Hola, el profesor mas honorable!'
	print >>sys.stderr, 'sending "%s"' % message
	sock.sendall(message)

	#Look for the response
	amount_received = 0
	amount_expected = len(message)

	while amount_received < amount_expected:
		data = sock.recv(32)
		amount_received += len(data)
		print >>sys.stderr, 'received "%s"' % data

finally:
	print >>sys.stderr, 'Closing socket..'
	sock.close()
