#Confeccionar un programa que permita ingresar dos números en controles de tipo Entry,
#luego sumar los dos valores ingresados y mostrar la suma en una Label al presionar un botón 

import tkinter as tk

class Aplicacion:
    def __init__(self):
        self.ventana=tk.Tk()
        self.label1=tk.Label(text="ingrese dos numeros para su suma")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana, width=10, textvariable=self.dato1)
        self.entry1.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana, width=10, textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        self.boton=tk.Button(self.ventana, text="sumar!", command=self.sumar)
        self.boton.grid(column=0, row=2)
        self.label2=tk.Label(text="Resultado")
        self.label2.grid(column=0, row=3)
        self.ventana.mainloop()

    def sumar(self):
        valor1=int(self.dato1.get())+int(self.dato2.get())
        self.label2.configure(text=valor1)

aplicacion1=Aplicacion()
