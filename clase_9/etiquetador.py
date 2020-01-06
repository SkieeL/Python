import tkinter as tk

# Crear ventana root
root = tk.Tk()

# Modificar la ventana
root.title("Etiquetador")
root.geometry("200x50")

# Creamos un frame en la ventana
frame = tk.Frame(root)
frame.grid()

# Creamos una etiqueta en el frame
lbl = tk.Label(frame, text="¡Soy una etiqueta!")
lbl.grid()

# Lanzar el ciclo de eventos
root.mainloop()
