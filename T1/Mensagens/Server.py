import socket
import threading
from time import sleep
from datetime import datetime

HOST = "192.168.246.32"
PORT = 9002

HOST_CLIENT1 = "192.168.246.32"
PORT_CLIENT1 = 9003

conexoes = []
fila = []

semaforo = threading.Semaphore(1)
semaforoFila = threading.Semaphore(1)

def receber_mensagem_cliente(conn, addr):
    print(f"[Server] Nova conexão {addr[0]}", flush=True)
    
    nome = conn.recv(1024).decode("utf-8")
    
    while True:
        mensagem = conn.recv(1024).decode("utf-8")
        
        
        hora = datetime.now().strftime("%H:%M:%S")  
        result = f"[{nome} ({addr[0]}) {hora}]\n{mensagem}"
        
        semaforoFila.acquire()
        fila.append(result)
        semaforoFila.release()
 
def enviar_mensagens_da_fila():
    while True :
        semaforoFila.acquire()
        for msg in fila:
            msg_bytes = msg.encode("utf-8") 
            
            for conn in conexoes:
                conn.sendall(msg_bytes)
        
        fila.clear()

def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()

        print(f"Servidor ouvindo em {HOST}:{PORT} para usuários")

        while True:
            conn, addr = server.accept()
            connR, addrR = server.accept()
            conexoes.append(connR)
            thread = threading.Thread(
                target=receber_mensagem_cliente,
                args=(conn, addr),
                daemon=True
            )
            thread.start()

    with socket.socket(socket.AD_INET, socket.SOCK_STREAM) as server2:
        server2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server2.bind((HOST_CLIENT1, PORT_CLIENT1))
        server2.listen()

        threadResposta = threading.Thread(enviar_mensagens_da_fila)
        threadResposta.start()

    
if __name__ == "__main__":
    iniciar_servidor()