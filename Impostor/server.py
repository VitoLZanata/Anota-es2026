# Servidor
import socket
import threading
import random


HOST = "0.0.0.0"
PORT = 9002
U = "utf-8"
N_J = 3
CONEXOES = [None] * N_J
NOMES = [None] * N_J
LETRA_COMPARTILHADA = [""]
barreira = threading.Barrier(N_J)
temas = ["Lugar", "Objeto", "Pessoa", "Animal", "Cor", "Fruta", "Profissão", "Filme", "País", "Esporte"]


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            # Permite reiniciar o servidor sem erro de "Address already in use"
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server.bind((HOST, PORT))
            server.listen()
            
            print(f"Servidor STOP rodando em {HOST}:{PORT}")
            print(f"Aguardando {N_J} jogadores...")
            
            idx = 0
            while idx < N_J:
                conn, addr = server.accept()
                CONEXOES[idx] = conn # Salva a conexão para uso futuro se precisar
                
                thread = threading.Thread(
                    target=jogo, 
                    args=(conn, addr, idx)
                )
                thread.start()
                idx += 1

def jogo(conn, addr, idx):
    conn.sendall("Digite seu nome(Os outros usuários verão): ".encode(U))
    nome = conn.recv(1024).decode(U).strip()
    print("Bem vindo(a) " + nome + "!")
    barreira.wait()
    while True:
        tema = randomizarTema()
        enviarMensagem(tema) 

def enviarMensagem(msg):
    for i in CONEXOES:
        i.sendall(msg.encode("U"))

def randomizarTema():
    return random.choice(temas)

if __name__ == "__main__":
    iniciar_servidor()