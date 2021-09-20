#Solicitar el ingreso del nombre de una persona y seleccionar de un control Combobox un país.
#Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.

import tkinter as tk
from tkinter import ttk

class hola:
    def __init__(self):
        self.ventana=tk.Tk()
        self.label1=ttk.Label(self.ventana, text="ingrese su nombre: ")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.ventana, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label3=ttk.Label(self.ventana, text="pais de origen: ")
        self.label3.grid(column=0, row=3)
        self.paises=tk.StringVar()
        paises=("argentina", "uruguay", "paraguay", "chile", "venezuela", "nicaragua", "salvador")
        self.opciones=ttk.Combobox(self.ventana, width=10, textvariable=self.paises, values=paises, state="readonly")
        self.opciones.current(0)
        self.opciones.grid(column=1, row=3)
        self.boton=ttk.Button(self.ventana, text="ejecutar", command=self.boton)
        self.boton.grid(column=1, row=4)
        self.label2=ttk.Label(self.ventana, text="nombre y pais")
        self.label2.grid(column=1, row=5)
        self.ventana.mainloop()

    def boton(self):
        self.label2.configure(text=self.dato1.get()+"\n"+self.paises.get())

aplicacion=hola()
