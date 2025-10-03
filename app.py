import socket

## Let's get time 

import time
import sys
from datetime import datetime

## Let's get time 

HOST = "0.0.0.0"   # Listen on all interfaces
PORT = 8080        # Port to listen on
count = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[*] Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            count += 1
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # get the time
            server_ip = conn.getsockname()[0]  # gets the server's own IP
            
            print(f"[{now}] [INFO] Connection #{count} from {addr}",flush=True)
       
            # Print Hello world with local ip
            body = f"Hello, World! 👋\nYou have hit pod ip : {server_ip}\nspace\n"
            response = (
                "HTTP/1.1 200 OK\r\n" 
                "Content-Type: text/plain\r\n"
                f"Content-Length: {len(body)}\r\n"
                "Connection: close\r\n"
                "\r\n"
                f"{body}"
            )
            conn.sendall(response.encode())
