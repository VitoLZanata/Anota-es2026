#Cliente 
import socket

HOST = ""
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = s.recv(1024).decode()
    print(msg)

    msg = s.recv(1024).decode()
    print(msg)

    while True:
        msg = s.recv(1024).decode()
        print(msg)

        if "Sua vez" in msg:
            jogada = input()
            s.sendall(jogada.encode())

        else:
            msg = s.recv(1024).decode()
            print(msg)

            if "venceu o jogo" in msg:
                break

    print("Fim de jogo!")