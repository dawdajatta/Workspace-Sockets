#!/usr/bin/env python
"""
A simple echo server
"""

import socket
import sys
import datetime

host = 'localhost'
port = 40000
backlog = 5
size = 512

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to the port
server_address = (host, port)
print >>sys.stderr, 'Starting up on %s port %s...' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(backlog)

while True:
	# Wait for command
	print >>sys.stderr, 'Waiting for a connection...'
	connection, client_address = sock.accept()

	try:
		print >>sys.stderr, 'connection from', client_address, 'at',
		while True:
			data = connection.recv(size)
			print >>sys.stderr, 'Received "%s"' % data
			if data:
				print >>sys.stderr, 'Sending data back to the client...'
				connection.sendall(data)
			else:
				print >>sys.stderr, 'No more data from', client_address
				break
	finally:
		#clean up the connection
		connection.close()
