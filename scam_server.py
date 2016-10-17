import socket
import sys

host = ''
port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	sock.bind((host, port))
except socket.error as msg:
	print('Bind failed. Error code: ' + str(msg[0]) + ' Message ' + msg[1])
	sys.exit()

print('Sock binding complete.')

# Listen on the socket
sock.listen(1)
print('Socket now listening.')


def readlines(sock, recv_buf=4096, delim='\n'):
	buf = ''
	data = True
	while data:
		data = sock.recv(recv_buf)
		buf += data

		while buf.find(delim) != -1:
			line, buf = buf.split('\n', 1)
			yield line

	return	

while True:
	print('Waiting for connections...')
	conn, addr = sock.accept()
	print('Connected with ' + addr[0] + ':' + str(addr[1]))
	while True:
		for line in readlines(conn):
			print(line)
			say_from_input(line)



sock.close()
