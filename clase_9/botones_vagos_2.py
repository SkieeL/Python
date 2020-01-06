import tkinter as tk


class Aplicacion(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.crear_componentes()

    def crear_componentes(self):
        # Creamos los botones
        self.bot1 = tk.Button(self, text="No hago nada")
        self.bot1.grid()

        self.bot2 = tk.Button(self)
        self.bot2.grid()
        self.bot2.configure(text="Yo tampoco")

        self.bot3 = tk.Button(self)
        self.bot3.grid()
        self.bot3["text"] = "Lo mismo por acá"


# Crear ventana root
root = tk.Tk()

# Modificar la ventana
root.title("Botones vagos 2 (con clase)")
root.geometry("200x85")

# Creamos un frame en la ventana
frame = Aplicacion(root)

# Lanzar el ciclo de eventos
root.mainloop()
