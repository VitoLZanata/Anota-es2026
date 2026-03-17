# Cliente
import socket

HOST = ""
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #conecta com o servidor 
    s.connect((HOST, PORT))
    msg = s.recv(1024).decode()  # -1 Você é o jogador X
    print(msg)

    msg = s.recv(1024).decode()  # -2 Aguardando jogador X conectar/jogar
    print(msg)

    msg = s.recv(1024).decode()  # -3 (Jogue)
    print(msg)

    jogada = input()
    s.sendall(jogada.encode())

    msg = s.recv(1024).decode()  # -4  Aguardando jogador jogar/ computando vencedor
    print(msg)

    msg = s.recv(1024).decode()  # -5 resultado
    print(msg)

    print("Fim de jogo!")

