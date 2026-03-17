# Cliente
import socket

HOST = ""
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #conecta com o servidor 
    s.connect((HOST, PORT))
    msg = s.recv(1024).decode()  # -1
    print(msg)

    msg = s.recv(1024).decode()  # -2
    print(msg)

    msg = s.recv(1024).decode()  # -3 (Jogue)
    print(msg)

    jogada = input()
    s.sendall(jogada.encode())

    msg = s.recv(1024).decode()  # -4
    print(msg)

    msg = s.recv(1024).decode()  # -5
    print(msg)

    print("Fim de jogo!")

