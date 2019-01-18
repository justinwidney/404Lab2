#!/usr/bin/env python3

import socket

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

addr_info = socket.getaddrinfo("www.google.com", 80, proto=socket.SOL_TCP)
(family, socketype, proto, canonname, sockaddr) = addr_info[0]



def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)      

        s.bind((HOST, PORT))
        s.listen(1)
       
    
        while True:
            conn, addr = s.accept() 
            print(conn)
            with conn:
                
                with socket.socket(family, socketype) as proxy_end:
                    
                    proxy_end.connect(sockaddr)
                    
                   
                    full_data = b""
                    while True:
                        data = conn.recv(BUFFER_SIZE)
                        if not data:
                           break
                        full_data += data
                    
                    proxy_end.sendall(full_data)
                    
                    data_google = b""
                    while True:
                        data = proxy_end.recv(BUFFER_SIZE)
                        if not data:
                            break
                        data_google += data
                    conn.sendall(data_google)
         
 

if __name__ == "__main__":
	main()
