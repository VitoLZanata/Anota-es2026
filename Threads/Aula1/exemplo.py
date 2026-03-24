import threading

def tarefa():
    print("Executando Tarefa...")
    
t = threading.Thread(target=tarefa)
t.start()
t.start

print("Finalizado")