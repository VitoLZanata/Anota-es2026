import socket

HOST = "0.0.0.0"
PORT = 9067

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print("Cliente:", addr)

        with conn:
            while True:
                data = conn.recv(1024)
                print("Martins:" + data.decode())
                msg = input("Servidor:")
                conn.sendall(msg.encode())

        print("desconectando")