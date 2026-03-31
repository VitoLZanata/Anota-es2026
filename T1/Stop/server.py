import socket
import threading
import random

HOST = "0.0.0.0"
PORT = 9002

NOME = ["", ""] 
CEP = ["", ""]

N_J = 5

ALFABETO = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
WAITING_TIME = 3
semaforo = threading.Semaphore(0)
semaforoJogadores = threading.Semaphore(N_J)

def atender_cliente(conn, addr, jogador_id, letraEscolhida):
    print(f"[Server] Nova conexão {addr}", flush=True)
    semaforo.acquire()

    with conn:
        data = conn.recv(1024)

        # Tema 1: Nome
        conn.sendall(("Nome com " + letraEscolhida + ":").encode("utf-8"))
        nome = conn.recv(1024).decode("utf-8")
        NOME[jogador_id] = nome

        # Tema 2: CEP
        conn.sendall("CEP:".encode("utf-8"))
        cep = conn.recv(1024).decode("utf-8")
        CEP[jogador_id] = cep

        

    semaforo.release()
    print(f"[Server] Conexão encerrada {addr}", flush=True)


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        pntsJ1, pntsJ2 = 0, 0
        print(f"Servidor ouvindo em {HOST}:{PORT}")

        conn, addr = server.accept()
        conn2, addr2 = server.accept()

        letraEscolhida = random.choice(ALFABETO)

        thread = threading.Thread(
            target=atender_cliente,
            args=(conn, addr, 0, letraEscolhida),
            daemon=True
        )
        thread2 = threading.Thread(
            target=atender_cliente,
            args=(conn2, addr2, 1, letraEscolhida),
            daemon=True
        )

        thread.start()
        thread2.start()

        semaforo.release()
        semaforo.release()

        thread.join()
        thread2.join()

        # Tema Nome
        if NOME[0] == NOME[1]:
            pntsJ1 += 1
            pntsJ2 += 1
        else:
            pntsJ1 += 3
            pntsJ2 += 3

        # Tema CEP
        if CEP[0] == CEP[1]:
            pntsJ1 += 1
            pntsJ2 += 1
        else:
            pntsJ1 += 3
            pntsJ2 += 3

        conn.sendall(f"Pontuação: {pntsJ1}".encode("utf-8"))
        conn2.sendall(f"Pontuação: {pntsJ2}".encode("utf-8"))

        print(f"Pontuação J1: {pntsJ1} | J2: {pntsJ2}")


if __name__ == "__main__":
    iniciar_servidor()