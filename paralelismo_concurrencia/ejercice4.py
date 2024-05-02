import threading

# Variables compartidas
counter = 100
size = 30
arra = [None]*size
ii = 0

# Función que incrementa una variable compartida de manera segura
def increment_counter1(lock):
    global counter, ii, arra
    for _ in range(50):
        # Bloqueamos el acceso a las variables compartidas
        lock.acquire()
        
        #arra.append(counter)  # Agregamos el valor de counter al final de arra
        
        if ii != 0 and ii % size == 0:
            ii = 0
        arra[ii] = counter
        counter += 1
        ii += 1
        print(f"Incrementando 1: counter = {counter}, ii = {ii}")
        lock.release()

# Función que incrementa otra variable compartida de manera segura
def increment_counter2(lock):
    global counter, ii, arra
    for _ in range(50):
        # Bloqueamos el acceso a las variables compartidas
        lock.acquire()
        
        #arra.append(counter)  # Agregamos el valor de counter al final de arra
        
        if ii != 0 and ii % size == 0:
            ii = 0
        arra[ii] = counter
        ii += 1
        counter += 1
        print(f"Incrementando 2: counter = {counter}, ii = {ii}")
        lock.release()

def main():
    global counter, ii, arra
    counter = 0
    ii = 0
    lock = threading.Lock()  # Creamos un objeto de bloqueo

    # Creamos dos hilos, uno para cada función
    increment_thread = threading.Thread(target=increment_counter2, args=(lock,))
    decrement_thread = threading.Thread(target=increment_counter1, args=(lock,))

    # Iniciamos ambos hilos
    increment_thread.start()
    decrement_thread.start()

    # Esperamos a que ambos hilos terminen
    increment_thread.join()
    decrement_thread.join()

    # Imprimimos el arreglo final
    print("Arreglo final:", arra)

    # Imprimimos el valor final del contador
    print("Valor final del contador:", counter)
    print(0%27)

if __name__ == "__main__":
    main()
