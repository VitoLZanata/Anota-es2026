import socket

HOST = "192.168.248.109"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))

    for _ in range(2):  # 2 temas: Nome e CEP
        # Recebe a solicitação do servidor
        solicitacao = cliente.recv(1024).decode("utf-8")
        print(f"[Server] {solicitacao}")

        # Pergunta ao usuário
        resposta = input("[Cliente] Resposta: ")
        cliente.sendall(resposta.encode("utf-8"))

    # Recebe a pontuação final
    pontuacao = cliente.recv(1024).decode("utf-8")
    print(f"[Server] {pontuacao}")