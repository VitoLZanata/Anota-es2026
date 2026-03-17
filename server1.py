# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    #Aguarda jogador
    print("[server] aguardando jogador1") 
    conn_1, addr_1 = s.accept()
    conn_1.sendall("[server] Ok. você é o jogador 1".encode()) # - 1
    conn_1.sendall("[server] aguardando jogador 2 conectar".encode()) # -2
    print("[server] aguardando jogador2") 
    conn_2, addr_2 = s.accept()
    conn_2.sendall("[server] Ok. você é o jogador 2".encode()) # - 1
    conn_2.sendall("[server] aguardando jogador 1 jogar".encode()) # -2
    conn_1.sendall("Jogue- (pedra, papel ou tesoura)".encode()) # -3
    jogadaJ1 = conn_1.recv(1024).decode()
    conn_1.sendall("Aguardando jogador 2".encode()) # -4
    conn_2.sendall("Jogue- (pedra, papel ou tesoura)".encode()) # -3
    jogadaJ2 = conn_2.recv(1024).decode()
    conn_2.sendall("Computando vencedor!".encode()) # -4

    if jogadaJ1 == jogadaJ2:
        msg = "Empatou kk"
    elif (
        (jogadaJ1 == "pedra" and jogadaJ2 == "tesoura") or
        (jogadaJ1 == "tesoura" and jogadaJ2 == "papel") or
        (jogadaJ1 == "papel" and jogadaJ2 == "pedra")
        ):
        msg =  "Jogador 1 venceu!"
    else:
        msg = "Jogador 2 venceu!"

    conn_1.sendall(msg.encode()) # -5
    conn_2.sendall(msg.encode()) # -5
    
    print(msg)

    print("Fim de jogo!")

    conn_1.close()
    conn_2.close()