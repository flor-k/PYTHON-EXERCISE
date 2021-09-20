#Disponer tres controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'.
# Cuando se presione un botón cambiar el color de fondo del formulario.
#Si consideramos que la variable ventana1 es un objeto de la clase Tk,
#luego si queremos que el fondo sea de color rojo debemos llamar al método configure y
#en el parámetro bg indicar un string con el color a activar ("red", "green" o "blue"):
#            self.ventana1.configure(bg="red")

import tkinter as tk

class hola:
    def __init__(self):
        self.ventana=tk.Tk()
        self.label1=tk.Label(text="seleccione color de fono")
        self.label1.grid(column=0, row=0)
        self.seleccion=tk.IntVar()
        self.seleccion.set(3)
        self.radio1=tk.Radiobutton(self.ventana,text="rojo", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=1)
        self.radio1=tk.Radiobutton(self.ventana,text="verde", variable=self.seleccion, value=2)
        self.radio1.grid(column=1, row=1)
        self.radio1=tk.Radiobutton(self.ventana,text="azul", variable=self.seleccion, value=3)
        self.radio1.grid(column=2, row=1)
        self.boton=tk.Button(self.ventana, text="color", command=self.color)
        self.boton.grid(column=2, row=2)
        self.ventana.mainloop()

    def color(self):
        if self.seleccion.get()==1:
            self.ventana.configure(bg="red")
        elif self.seleccion.get()==2:
            self.ventana.configure(bg="green")
        else:
            self.ventana.configure(bg="blue")




aplicacion1=hola()

