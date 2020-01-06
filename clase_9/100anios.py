import tkinter as tk


class Aplicacion(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.crear_componentes()

    def crear_componentes(self):
        self.lbl_instrucciones = tk.Label(
            self, text="Ingresar password para obtener el secreto para vivir 100 años"
        )
        self.lbl_instrucciones.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=tk.W
        )

        self.lbl_password = tk.Label(
            self, text="Password: "
        )
        self.lbl_password.grid(
            row=1,
            column=0,
            sticky=tk.W
        )

        self.txt_password = tk.Entry(self)
        self.txt_password.grid(
            row=1,
            column=1,
            sticky=tk.W
        )

        self.btn_enviar = tk.Button(
            self,
            text="Enviar",
            command=self.revelar
        )
        self.btn_enviar.grid(
            row=2,
            column=0,
            sticky=tk.W
        )

        self.txt_secreto = tk.Text(
            self,
            width=35,
            height=5,
            wrap=tk.WORD
        )
        self.txt_secreto.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky=tk.W
        )

    def revelar(self):
        contenido = self.txt_password.get()

        if contenido == "secreto":
            mensaje = "Este es el secreto para vivir 100 años: "
            mensaje += "viví 99 y después tené MUCHO cuidado."
        else:
            mensaje = "Esa password es incorrecta, "
            mensaje += "no puedo compartir el secreto con vos."

        self.txt_secreto.delete(0.0, tk.END)
        self.txt_secreto.insert(0.0, mensaje)


# Crear ventana root
root = tk.Tk()

# Modificar la ventana
root.title("Cómo llegar a los 100 años")
root.geometry("300x150")

# Creamos un frame en la ventana
frame = Aplicacion(root)

# Lanzar el ciclo de eventos
root.mainloop()
