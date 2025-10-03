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
            ## Time 
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ## Time 
            print(f"[{now}] [INFO] Connection #{count} from {addr}",flush=True)
            conn.sendall(f"Connection count: {count}\n".encode())
