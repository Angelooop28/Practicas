import datetime 
import threading, time, os
import tkinter as tk

##EJEMPLO DE HILOS Y SUS METODOS GRUPO 2

def hora():
    while True:
            try:
                hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
                label.config(text=hora_actual)
                print(threading.get_ident(), hora_actual)
                time.sleep(1)
            except InterruptedError :
                 print("Se interrumpio el hilo por un segundo")

def detener():
    root.quit
    os._exit(os.EX_OK)

def status():
    print(hilo_hora.is_alive())

def interrumpir():
    #emula el metodo Join ya que no se puede cambiar el estado porque calramente solo hay un proceso es decir un solo hilo
    print("Se interrumpio el hilo durante un segundo")

hilo_hora = threading.Thread(target=hora)

root = tk.Tk()
label = tk.Label(root, font=("Arial", 20))
label.pack()
root.title("RELOJ")
root.geometry("300x200")
btn = tk.Button(root, text="Iniciar reloj", command= lambda: hilo_hora.start())
btn.pack()
btn = tk.Button(root, text="Detener", command=  lambda: detener())
btn.pack()
btn = tk.Button(root, text="Estado", command=  lambda: status())
btn.pack()
btn = tk.Button(root, text="Interrumpir", command=  lambda: interrumpir())
btn.pack()
root.mainloop()