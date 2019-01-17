import socket
from multiprocessing import Pool

HOST = "localhost"
PORT = 8081
BUFFER_SIZE = 1024

payload = """GET / HTTP/1.0
Host: {HOST}

""".format(HOST=HOST)

def conn_socket(addr_tup):
    (family, socktype, proto, canonname, sockaddr) = addr_tup
    try:
        s = socket.socket(family,socktype,proto)
        s.connect(sockaddr)
 	full_data = b""
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
       

        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            full_data += data

        print(full_data)

    except e: 
        print(e)
    finally:
        s.close()        

def main():

    addr_info = socket.getaddrinfo(HOST, PORT, proto=socket.SOL_TCP)    
    
    addr = addr_info[1]
    with Pool() as p:
        p.map(conn_socket, [addr_tup for _ in range(1,50)])
      
       

if __name__ == "__main__":
main()
