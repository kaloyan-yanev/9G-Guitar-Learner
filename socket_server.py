import socket
import time

HOST = "127.0.0.1"
PORT = 64000

# create socket and listen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print(f"Listening on {HOST}:{PORT}")

# accept connection
conn, addr = s.accept()
print(f"Accepted connection from {HOST}:{PORT}")

cmd = ""
while True:
    data = conn.recv(64)
    time.sleep(1)
    if not data:
        break
    print(data.decode())
    info = data.decode()
    conn.sendall(b"OK")  

conn.sendall(b"Finished")
s.close()
nodes = info.split(',')
for nodes in nodes:
    print(nodes)