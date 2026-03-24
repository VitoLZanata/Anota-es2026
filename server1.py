# Servidor
import socket

HOST = "0.0.0.0"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    print("[server] aguardando jogador1") 
    conn_1, addr_1 = s.accept()
    conn_1.sendall("[server] Ok. você é o jogador 1".encode())
    conn_1.sendall("[server] aguardando jogador 2 conectar".encode())

    print("[server] aguardando jogador2") 
    conn_2, addr_2 = s.accept()
    conn_2.sendall("[server] Ok. você é o jogador 2".encode())
    conn_2.sendall("[server] aguardando jogador 1 jogar".encode())

    pontos_j1 = 0
    pontos_j2 = 0

    while True:
        conn_1.sendall("Jogue- (pedra, papel ou tesoura)".encode())
        jogadaJ1 = conn_1.recv(1024).decode()
        conn_1.sendall("Aguardando jogador 2 jogar".encode())

        conn_2.sendall("Jogue- (pedra, papel ou tesoura)".encode())
        jogadaJ2 = conn_2.recv(1024).decode()
        conn_2.sendall("Computando vencedor!".encode())

        if jogadaJ1 == jogadaJ2:
            msg = "Empatou kk"
        elif (
            (jogadaJ1 == "pedra" and jogadaJ2 == "tesoura") or
            (jogadaJ1 == "tesoura" and jogadaJ2 == "papel") or
            (jogadaJ1 == "papel" and jogadaJ2 == "pedra")
        ):
            msg = "Jogador 1 venceu!"
            pontos_j1 += 1
            if pontos_j2 > 0:
                pontos_j2 -= 1
        else:
            msg = "Jogador 2 venceu!"
            pontos_j2 += 1
            if pontos_j1 > 0:
                pontos_j1 -= 1

        placar = "Placar -> J1: " + str(pontos_j1) + " | J2: " + str(pontos_j2)

        conn_1.sendall((msg + "\n" + placar).encode())
        conn_2.sendall((msg + "\n" + placar).encode())

        print(msg)
        print(placar)

        if pontos_j1 >= 3 or pontos_j2 >= 3:
            if pontos_j1 >= 3:
                final = "Jogador 1 venceu o jogo!"
            else:
                final = "Jogador 2 venceu o jogo!"

            conn_1.sendall(final.encode())
            conn_2.sendall(final.encode())
            print(final)
            break

    print("Fim de jogo!")

    conn_1.close()
    conn_2.close()