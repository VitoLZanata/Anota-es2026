# Cliente
import socket

HOST = "127.0.0.1"
PORT = 9002
U = "utf-8"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"ola socket")

    m = input(s.recv(1024).decode(U) + ": ")
    s.sendall(m.encode(U)).strip()
    