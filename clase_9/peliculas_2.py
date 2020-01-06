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
            text="Seleccioná uno"
        ).grid(
            row=1, column=0, sticky=tk.W
        )

        # Creamos un objeto StringVar, que será asignado en función de
        # la opción que se seleccionó.
        self.favorito = tk.StringVar()
        self.favorito.set(None)

        tk.Radiobutton(
            self,
            text="Comedia",
            variable=self.favorito,
            value="comedia.",
            command=self.actualizar_texto
        ).grid(
            row=2, column=0, sticky=tk.W
        )

        tk.Radiobutton(
            self,
            text="Acción",
            variable=self.favorito,
            value="acción.",
            command=self.actualizar_texto
        ).grid(
            row=3, column=0, sticky=tk.W
        )

        tk.Radiobutton(
            self,
            text="Drama",
            variable=self.favorito,
            value="drama.",
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
        mensaje = "Tu tipo favorito de película es: " + self.favorito.get()

        self.txt_resultados.delete(0.0, tk.END)
        self.txt_resultados.insert(0.0, mensaje)


# Crear ventana root
root = tk.Tk()

# Modificar la ventana
root.title("Películas 2")
# Nota: al no asignarle las dimensiones a mano, notar que la ventana se adapta
# a los componentes.

# Creamos un frame en la ventana
frame = Aplicacion(root)

# Lanzar el ciclo de eventos
root.mainloop()
