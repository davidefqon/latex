import threading
import time
# Función que será ejecutada por cada hilo
def thread_function(thread_id):
    print("Hilo", thread_id, "ejecutando...")
    time.sleep(1) # Simulamos algo de trabajo en el hilo
    print("Hilo", thread_id, "terminado.")
def main():
    num_threads = 5
    threads = []
    # Crear varios hilos
    for i in range(num_threads):
        thread = threading.Thread(target=thread_function, args=(i,))
        threads.append(thread)
        thread.start()
    # Esperar a que todos los hilos terminen su ejecución
    for thread in threads:
        thread.join()
    print("Todos los hilos han terminado.")

if __name__ == "__main__":
    main()
