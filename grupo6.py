import random
import matplotlib.pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation

# Inicializamos una lista para almacenar los datos de temperatura
temperatura = []
index = count()

def update_temperatura(i):
    global temperatura  # Declarar la variable como global
    
    # Generamos un dato de temperatura aleatorio entre 0 y 100
    temperaturas = random.uniform(0, 100)
    
    # Agregamos el dato a la lista
    temperatura.append(temperaturas)
    
    # Limitamos la lista a las últimas 20 muestras para mantener la ventana en tiempo real
    temperatura = temperatura[-20:]
    
    # Limpiamos el gráfico
    plt.cla()
    
    # Graficamos los datos
    plt.plot(temperatura, marker='o', linestyle='-')
    
    # Configuramos el título y etiquetas
    plt.title("Monitoreo de Temperatura en Tiempo Real")
    plt.xlabel("Muestras")
    plt.ylabel("Temperatura (°C)")
    
    # Actualizamos el gráfico
    plt.tight_layout()

# Creamos una figura para el gráfico
plt.figure(figsize=(8, 4))

# Creamos una animación que actualice los datos cada segundo
ani = FuncAnimation(plt.gcf(), update_temperatura, interval=1000)

# Mostramos el gráfico en tiempo real
plt.show()