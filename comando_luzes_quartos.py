import serial
import time
import tkinter as tk
from tkinter import messagebox

porta = 'COM4'
baudrate = 9600

try:
    arduino = serial.Serial(porta, baudrate, timeout=1)
    time.sleep(2)
except serial.SerialException:
    messagebox.showerror("Erro", f"Não foi possível conectar à porta {porta}.")
    exit()


estado_1 = False
estado_2 = False

def enviar_comando(comando):
    try:
        arduino.write((comando + "\n").encode())
        time.sleep(0.1)
    except:
        messagebox.showerror("Erro", "Falha ao enviar comando ao Arduino.")

def atualizar_status():
    label_status_1.config(text="Acesa" if estado_1 else "Apagada", fg="white")
    label_status_2.config(text="Acesa" if estado_2 else "Apagada", fg="white")
    frame_1.config(bg="red" if estado_1 else "#660000")
    frame_2.config(bg="blue" if estado_2 else "#000066")

def acender_1():
    global estado_1
    enviar_comando("acender 1")
    estado_1 = True
    atualizar_status()

def apagar_1():
    global estado_1
    enviar_comando("apagar 1")
    estado_1 = False
    atualizar_status()

def acender_2():
    global estado_2
    enviar_comando("acender 2")
    estado_2 = True
    atualizar_status()

def apagar_2():
    global estado_2
    enviar_comando("apagar 2")
    estado_2 = False
    atualizar_status()

def sair():
    if messagebox.askokcancel("Sair", "Deseja encerrar o programa?"):
        root.destroy()
        if arduino.is_open:
            arduino.close()


root = tk.Tk()
root.title("Controle de Entradas Arduino")
root.geometry("600x300")
root.protocol("WM_DELETE_WINDOW", sair)


frame_1 = tk.Frame(root, bg="#660000", width=300, height=300)
frame_1.pack(side="left", fill="both", expand=True)

label_titulo_1 = tk.Label(frame_1, text="QUARTO 1", font=("Arial", 16), bg="#660000", fg="white")
label_titulo_1.pack(pady=10)

label_status_1 = tk.Label(frame_1, text="Apagada", font=("Arial", 14), bg="#660000", fg="white")
label_status_1.pack(pady=10)

btn_acender_1 = tk.Button(frame_1, text="Acender", command=acender_1, width=15)
btn_acender_1.pack(pady=5)

btn_apagar_1 = tk.Button(frame_1, text="Apagar", command=apagar_1, width=15)
btn_apagar_1.pack(pady=5)


frame_2 = tk.Frame(root, bg="#000066", width=300, height=300)
frame_2.pack(side="right", fill="both", expand=True)

label_titulo_2 = tk.Label(frame_2, text="QUARTO 2", font=("Arial", 16), bg="#000066", fg="white")
label_titulo_2.pack(pady=10)

label_status_2 = tk.Label(frame_2, text="Apagada", font=("Arial", 14), bg="#000066", fg="white")
label_status_2.pack(pady=10)

btn_acender_2 = tk.Button(frame_2, text="Acender", command=acender_2, width=15)
btn_acender_2.pack(pady=5)

btn_apagar_2 = tk.Button(frame_2, text="Apagar", command=apagar_2, width=15)
btn_apagar_2.pack(pady=5)


root.mainloop()
