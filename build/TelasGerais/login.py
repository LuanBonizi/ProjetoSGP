from pathlib import Path

from tkinter import *
from .telaPrincipal import TelaPrincipal


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / Path("assets/login")


user = 'sgp@gmail.com'
password = '1234'


class InterfaceLogin:
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Login")

        self.window.geometry("672x861")
        self.window.configure(bg = "#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 861,
            width = 672,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            24.0,
            24.0,
            672.0,
            861.0,
            fill="#548AFF",
            outline="")

        self.canvas.create_rectangle(
            0.0,
            0.0,
            648.0,
            837.0,
            fill="#F2F2F3",
            outline="")

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            324.0,
            152.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            249.0,
            280.0,
            anchor="nw",
            text="LOGIN",
            fill="#548AFF",
            font=("Inter Bold", 48 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_logar = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.login(),
            relief="flat"
        )
        self.button_logar.place(
            x=73.0,
            y=691.0,
            width=501.0,
            height=57.0
        )

        self.canvas.create_text(
            60.0,
            334.0,
            anchor="nw",
            text="Sistema de Gerenciamento de Projetos - SGP",
            fill="#000000",
            font=("Inter Bold", 24 * -1, 'bold')
        )
        
        self.entrada_senha = Entry(
            font= ('Arial',20),
            bd=0,
            bg="#B9BEEB",
            fg="#000716",
            highlightthickness=0,
            show = '*'
        )
        self.entrada_senha.place(
            x=73.0,
            y=568.0,
            width=501.0,
            height=55.0
        )

        self.canvas.create_text(
            72.0,
            525.0,
            anchor="nw",
            text="Senha:",
            fill="#1B1A1A",
            font=("Inter Bold", 28 * -1,'bold')
        )

        self.credenciais = self.canvas.create_text(
            73.0,
            629.0,
            anchor="nw",
            text="Credenciais inválidas!",
            fill="#FC0000",
            font=("Inter", 24 * -1)
        )
        
        self.canvas.itemconfig(self.credenciais,state='hidden')

        self.entrada_email = Entry(
            font= ('Arial',20),
            bd=0,
            bg="#B9BEEB",
            fg="#000716",
            highlightthickness=0
        )
        self.entrada_email.place(
            x=73.0,
            y=446.0,
            width=501.0,
            height=55.0
        )

        self.canvas.create_text(
            71.0,
            408.0,
            anchor="nw",
            text="E-mail: ",
            fill="#1B1A1A",
            font=("Inter Bold", 28 * -1,'bold')
        )
        self.window.resizable(False, False)

    def inicializa(self):
        self.window.mainloop()
    
    def relative_to_assets(self, path: str):
        return ASSETS_PATH / Path(path)

    def login(self):
        senha = self.entrada_senha.get()
        email = self.entrada_email.get()
        if email == user and senha == password:
            self.window.destroy()
            principal = TelaPrincipal()
            principal.abrePrincipal()
        else:
            self.canvas.itemconfig(self.credenciais,state='normal')