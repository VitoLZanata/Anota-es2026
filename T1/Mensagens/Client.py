import socket
from datetime import datetime

HOST = "192.168.246.32"
PORT = 9002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))

    # Ip pega pelo addr[0]
    # Digitar o nome - 
    nome = input("[Cliente] Digite seu nome: ")
    
    cliente.sendall(nome.encode("utf-8"))

    while True :
        mensagem = input("Digite sua mensagem: ")
        cliente.sendall(mensagem.encode("utf-8"))
    