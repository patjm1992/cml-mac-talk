import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 9999))

while True:
	thing = raw_input('What to say? ')
	thing += '\n'
	sock.sendall(thing.encode())

sock.close