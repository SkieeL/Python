import tkinter as tk


class Aplicacion(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.clicks = 0
        self.crear_componentes()

    def crear_componentes(self):
        # Creamos el botón
        self.boton = tk.Button(self)
        self.boton["text"] = "Clicks: 0"
        self.boton["command"] = self.actualizar_contador
        self.boton.grid()

    def actualizar_contador(self):
        self.clicks += 1
        self.boton["text"] = "Clicks: " + str(self.clicks)
        print("Clicks:", self.clicks)


# Crear ventana root
root = tk.Tk()

# Modificar la ventana
root.title("Contador de clicks")
root.geometry("200x85")

# Creamos un frame en la ventana
frame = Aplicacion(root)

# Lanzar el ciclo de eventos
root.mainloop()
