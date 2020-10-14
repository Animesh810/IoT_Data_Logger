import socket

HOST = '192.168.1.7' # Server IP or Hostname
PORT = 12359 # Pick an open Port (1000+ recommended), must match the client port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

#managing error exception
try:
	s.bind((HOST, PORT))

except socket.error:
	print ('Bind failed ')

s.listen(20)
print ('Socket awaiting messages')
(conn, addr) = s.accept()
print ('Connected')

# awaiting for message

try:
	while True:
		data = conn.recv(100)
		data = data.decode()
		#data = eval(data)
		print ('Received: {} '.format(data) )
		#conn.close() # Close connections

except KeyboardInterrupt:
	conn.close()
