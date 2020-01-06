import tkinter as tk

# Crear ventana root
root = tk.Tk()

# Modificar la ventana
root.title("Botones vagos")
root.geometry("200x85")

# Creamos un frame en la ventana
frame = tk.Frame(root)
frame.grid()

# Creamos los botones
bot1 = tk.Button(frame, text="No hago nada")
bot1.grid()

bot2 = tk.Button(frame)
bot2.grid()
bot2.configure(text="Yo tampoco")

bot3 = tk.Button(frame)
bot3.grid()
bot3["text"] = "Lo mismo por acá"

# Lanzar el ciclo de eventos
root.mainloop()
