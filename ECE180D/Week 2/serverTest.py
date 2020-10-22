import socket
# The second line is initialization to add TCP/IP protocol to the endpoint.
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assigns a port for the server that listens to clients connecting to this port.
serv.bind(('0.0.0.0', 22))
serv.listen(5)
while True:
	conn, addr = serv.accept()
	from_client = b''
	while True:
		data = conn.recv(4096)
		if not data: break
		from_client += data
		print(from_client)
		conn.send(b'I am SERVER\n')
	conn.close()
	print('client disconnected')