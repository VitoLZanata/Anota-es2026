# Cliente
import socket

HOST = "192.168.246.106"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"ola mundo")
    print(s.recv(1024).decode())