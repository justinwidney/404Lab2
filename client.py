import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("www.google.com", 80))
request = "GET / HTTP/1.1\nHost: www.google.com\n\n"

request = str.encode(request)
s.send(request)
result = s.recv(10000)

while(len(result) > 0):
	print(result)
	result = s.recv(10000)

