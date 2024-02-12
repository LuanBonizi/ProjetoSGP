from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from Cadastro.cadastroCliente import CadastroCliente
from Cadastro.cadastroProjeto import CadastroProjeto
from .telaInicial import TelaInicial
from Visualizacao.visualizarClientes import VisualizarClientes
from Visualizacao.visualizarProjetos import VisualizarProjetos


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / Path("assets/telaPrincipal")


class TelaPrincipal:
    def __init__(self):
        
        self.root = Tk()
        self.root.title("Tela Principal")
        self.root.geometry("1440x1024")
        self.root.configure(bg = "#548AFF")


        self.canvas = Canvas(
            self.root,
            bg = "#548AFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_text(
            275.0,
            0.0,
            anchor="nw",
            text="Sistema de Gerenciamento de Projetos",
            fill="#FFFFFF",
            font=("Inter SemiBold", 48 * -1,'bold')
        )

        self.canvas.create_rectangle(
            0.0,
            75.0,
            333.0,
            1024.0,
            fill="#E7E7E7",
            outline="")

        linha = self.canvas.create_line(333,75,333,1024, fill="black", width=2, tags="linha")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.visualizarClientes(),
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=648.0,
            width=333.0,
            height=83.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.visualizarProjetos(),
            relief="flat"
        )
        self.button_2.place(
            x=0.0,
            y=565.0,
            width=333.0,
            height=83.0
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.telaCadastroProjeto(),
            relief="flat"
        )
        self.button_3.place(
            x=0.0,
            y=307.0,
            width=333.0,
            height=83.0
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.telaCadastroCliente(),
            relief="flat"
        )
        self.button_4.place(
            x=0.0,
            y=390.0,
            width=333.0,
            height=83.0
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.telaInicial(),
            relief="flat"
        )
        self.button_5.place(
            x=0.0,
            y=75.0,
            width=333.0,
            height=64.45569610595703
        )

        self.button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=0.0,
            y=485.0,
            width=333.0,
            height=80.0
        )

        self.button_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=0.0,
            y=227.0,
            width=333.0,
            height=80.0
        )

        self.canvas.create_rectangle(
            -10.0,
            65.0,
            1440.0,
            75.0,
            fill="#FFFFFF",
            outline="")

        linha = self.canvas.create_line(333,75,333,1024, fill="black", width=1, tags="linha")
        self.canvas.tag_raise("linha")
        
        self.frame = TelaInicial(self.root)

        self.root.resizable(False, False)
        
    def relative_to_assets(self, path: str):
        return ASSETS_PATH / Path(path)
    
    def abrePrincipal(self):
        self.root.mainloop()
    
    def telaInicial(self):
        self.frame = TelaInicial(self.root)
        
    def telaCadastroProjeto(self):
        self.frame = CadastroProjeto(self.root)
        
    def telaCadastroCliente(self):
        self.frame = CadastroCliente(self.root, None)
    
    def visualizarClientes(self):
        self.frame = VisualizarClientes(self.root)
    
    def visualizarProjetos(self):
        self.frame = VisualizarProjetos(self.root)
    
