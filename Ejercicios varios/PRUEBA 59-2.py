#Ingresar el nombre de usuario y clave en controles de tipo Entry.
# Si se ingresa las cadena (usuario: juan, clave="abc123")
# luego mostrar en el título de la ventana el mensaje "Correcto"
# en caso contrario mostrar el mensaje "Incorrecto".
#Para mostrar '*' cuando se ingresa la clave debemos pasar en el parámetro
# 'show' el caracter a mostrar:
#        self.entry2=tk.Entry(self.ventana1, width=30, textvariable=self.dato2, show="*")

import tkinter as tk

class hola:
    def __init__(self):
        self.ventana=tk.Tk()
        self.nombre="juan"
        self.clave="abc123"
        self.label1=tk.Label(text="Ingrese nombre: ")
        self.label1.grid(column=0, row=0)
        self.label2=tk.Label(text="ingrese clave: ")
        self.label2.grid(column=0, row=1)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana, width=20, textvariable=self.dato2, show="*")
        self.entry2.grid(column=1, row=1)
        self.boton1=tk.Button(self.ventana, text="verificar", command=self.boton)
        self.ventana.mainloop()
        

    def boton(self):
        if self.dato1.get()=="juan" and self.dato2.get()=="abc123":
            self.ventana.title("Correcto")
        else:
            self.ventana.title("Incorrecto")
aplicacion1=hola()

