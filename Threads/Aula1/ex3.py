import threading
import time

TEMPO_ESPERA = 0.1

# Semáforo
semaforo = threading.Semaphore(0)

def thread_0():
    for i in range(1, 11):
        semaforo.acquire()
    
        print(f"[Thread 0] {i}", flush=True)
    
        semaforo.release()
        time.sleep(TEMPO_ESPERA)


def thread_1():
    for i in range(1, 11):
        semaforo.acquire()
        
        print(f"[Thread 1] {i}", flush=True)
    
        semaforo.release()
        time.sleep(TEMPO_ESPERA)


# Instancia as threads
t0 = threading.Thread(target=thread_0)
t1 = threading.Thread(target=thread_1)

# Starta as threads
t0.start()
t1.start()

# Libera o semáforo
semaforo.release()

# Aguarda as threads finalizarem
print("[Main] Aguardando threads")
t0.join()
t1.join()

# Finalização
print("[Main] Finalizado")