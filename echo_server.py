import socket



HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1) 
       
        while True:
            conn, addr = s.accept() 
            full_data = b""
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                full_data += data

            print(full_data)
            conn.sendall(full_data)
            print(full_data)

if __name__ == "__main__":
	main()
