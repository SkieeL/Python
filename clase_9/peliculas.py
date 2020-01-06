import tkinter as tk


class Aplicacion(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.crear_componentes()

    def crear_componentes(self):
        tk.Label(
            self,
            text="Elegí tu tipo de película favorita"
        ).grid(
            row=0, column=0, sticky=tk.W
        )

        tk.Label(
            self,
            text="Seleccioná todos los que apliquen"
        ).grid(
            row=1, column=0, sticky=tk.W
        )

        self.le_gusta_comedia = tk.BooleanVar()
        tk.Checkbutton(
            self,
            text="Comedia",
            variable=self.le_gusta_comedia,
            command=self.actualizar_texto
        ).grid(
            row=2, column=0, sticky=tk.W
        )

        self.le_gusta_accion = tk.BooleanVar()
        tk.Checkbutton(
            self,
            text="Acción",
            variable=self.le_gusta_accion,
            command=self.actualizar_texto
        ).grid(
            row=3, column=0, sticky=tk.W
        )

        self.le_gusta_drama = tk.BooleanVar()
        tk.Checkbutton(
            self,
            text="Drama",
            variable=self.le_gusta_drama,
            command=self.actualizar_texto
        ).grid(
            row=4, column=0, sticky=tk.W
        )

        self.txt_resultados = tk.Text(
            self,
            width=40,
            height=5,
            wrap=tk.WORD
        )
        self.txt_resultados.grid(
            row=5,
            column=0,
            columnspan=3
        )

    def actualizar_texto(self):
        le_gusta = ""

        if self.le_gusta_comedia.get():
            le_gusta += "Te gustan las películas de comedia.\n"

        if self.le_gusta_accion.get():
            le_gusta += "Te gustan las películas de acción.\n"

        if self.le_gusta_drama.get():
            le_gusta += "Te gustan las películas de drama.\n"

        self.txt_resultados.delete(0.0, tk.END)
        self.txt_resultados.insert(0.0, le_gusta)


# Crear ventana root
root = tk.Tk()

# Modificar la ventana
root.title("Películas")
root.geometry("300x150")

# Creamos un frame en la ventana
frame = Aplicacion(root)

# Lanzar el ciclo de eventos
root.mainloop()
