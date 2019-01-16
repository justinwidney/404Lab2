import socket


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind(('0.0.0.0', 8001))
connection.listen(10)

while True:
    current_connection, address = connection.accept()
    data = current_connection.recv(2048)    
    current_connection.send(data)
    print (data)


