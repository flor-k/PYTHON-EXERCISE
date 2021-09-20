#Solicitar el ingreso del nombre de una persona y seleccionar de un control Listbox un país.
#Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado

import tkinter as tk

class hola:
    def __init__(self):
        self.ventana=tk.Tk()
        self.label1=tk.Label(self.ventana, text="ingrese su nombre:")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.barra=tk.Scrollbar(self.ventana, orient=tk.VERTICAL)
        self.lista=tk.Listbox(self.ventana, yscrollcommand=self.barra.set)
        self.lista.grid(column=0, row=1)
        self.barra.configure(command=self.lista.yview)
        self.barra.grid(column=1, row=1, sticky='NS')
        self.lista.insert(1, "argentina")
        self.lista.insert(2, "bolivia")
        self.lista.insert(3, "uruguay")
        self.lista.insert(4, "venezuela")
        self.lista.insert(5, "chile")
        self.lista.insert(5, "paraguay")
        self.lista.insert(5, "salvador")
        self.lista.insert(5, "nicaragua")
        self.lista.insert(5, "costa rica")
        self.lista.insert(5, "mexico")
        self.lista.insert(5, "costa rica")
        self.lista.insert(5, "mexico")
        self.lista.insert(5, "costa rica")
        self.lista.insert(5, "mexico")
        self.boton1=tk.Button(self.ventana, text="ejecutar", command=self.boton)
        self.boton1.grid(column=0, row=2)
        self.label2=tk.Label(self.ventana, text="")
        self.label2.grid(column=0, row=3)
        self.ventana.mainloop()

    
    def boton(self):
        if len(self.lista.curselection())!=0:
            self.label2.configure(text=self.dato1.get()+"\n"+self.lista.get(self.lista.curselection()[0]))

aplicacion=hola()