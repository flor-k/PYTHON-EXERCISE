#Mediante dos controles de tipo Entry permitir el ingreso de dos números.
#Crear un menú que contenga una opción que cambie el tamaño de la ventana con los valores
#ingresados por teclado.
#Finalmente disponer otra opción que finalice el programa

import tkinter as tk
import sys

class hola:
    def __init__(self):
        self.ventana=tk.Tk()
        self.label1=tk.Label(self.ventana, text="ingrese primer valor: ")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(self.ventana, text="ingrese segundo valor: ")
        self.label2.grid(column=0, row=1)
        self.valor1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana, width=10, textvariable=self.valor1)
        self.entry1.grid(column=1, row=0)
        self.valor2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana, width=10, textvariable=self.valor2)
        self.entry2.grid(column=1, row=1)
        self.label3=tk.Label(self.ventana, text="seleccione dentro del menu \n opcion para cambiar tamaño")
        menu1=tk.Menu(self.ventana)
        self.ventana.configure(menu=menu1)
        opcion1=tk.Menu(menu1, tearoff=0)
        opcion1.add_command(label="cambiar resolucion", command=self.resolucion, accelerator="Ctrl+C")
        opcion1.add_separator()
        opcion1.add_command(label="finalizar programa", command=self.final, accelerator="Ctrl+F")
        self.ventana.bind_all("<Control-c>", self.cambiar)
        self.ventana.bind_all("<Control-f>", self.cambiar)
        menu1.add_cascade(label="opciones", menu=opcion1)
        self.ventana.mainloop()

    def resolucion(self):
        self.ventana.geometry(self.valor1.get()+"x"+self.valor2.get())

    def final(self):
        sys.exit()

    def cambiar(self, event):
        if event.keysym=="c":
            self.resolucion()
        if event.keysym=="f":
            self.final()

aplicacion=hola()
