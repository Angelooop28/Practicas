

import threading

# Crear dos objetos de bloqueo
lock_A = threading.Lock()
lock_B = threading.Lock()

# Definir la función del hilo 1
def thread_1():
    # Adquirir el lock A
    lock_A.acquire()
    print("Hilo 1 tiene el lock A")
    # Intentar adquirir el lock B
    lock_B.acquire()
    print("Hilo 1 tiene el lock B")

# Definir la función del hilo 2
def thread_2():
    # Adquirir el lock B
    lock_B.acquire()
    print("Hilo 2 tiene el lock B")
    # Intentar adquirir el lock A
    lock_A.acquire()
    print("Hilo 2 tiene el lock A")


# Crear dos hilos
t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)

# Iniciar los hilos
t1.start()
t2.start()


# Esperar a que terminen los hilos
t1.join()
t2.join()

print("FINISH")

