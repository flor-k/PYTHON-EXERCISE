#Disponer varios objetos de la clase Checkbutton con nombres de navegadores web.
#En el título de la ventana mostrar todos los nombres de navegadores seleccionados.  

import tkinter as tk

class hola:
    def __init__(self):
        self.ventana=tk.Tk()
        self.label1=tk.Label(self.ventana, text="ingrese su navegador")
        self.label1.grid(column=0, row=0)
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana, text="chrome", variable=self.seleccion1)
        self.check1.grid(column=0, row=1)
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana, text="firefox", variable=self.seleccion2)
        self.check2.grid(column=1, row=1)
        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana, text="explorer", variable=self.seleccion3)
        self.check3.grid(column=2, row=1)
        self.boton1=tk.Button(self.ventana, text="ejecutar", command=self.boton)
        self.boton1.grid(column=0, row=2)
        self.ventana.mainloop()

    def boton(self):
        vari="browsers: "
        if self.seleccion1.get()==1:
            vari=vari+"chrome "
        if self.seleccion2.get()==1:
            vari=vari+"firefox "
        if self.seleccion3.get()==1:
            vari=vari+"explorer "
        self.ventana.title(vari)      

aplicacion=hola()