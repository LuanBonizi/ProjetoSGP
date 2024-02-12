from pathlib import Path
from tkinter import *

from tkinter import filedialog, messagebox
from PIL import Image, ImageGrab
from datetime import datetime
from reportlab.pdfgen import canvas


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / Path("assets/impressaoProjeto")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ImprimeProjeto:
    
    def __init__(self, projeto):
        self.window = Toplevel()
        self.window.title("Impressão de Projeto")

        self.window.geometry("1107x949")
        self.window.configure(bg = "#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 949,
            width = 1107,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1107.0,
            949.0,
            fill="#FFFFFF",
            outline="")

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            697.5,
            757.0,
            image=self.entry_image_1
        )
        self.descricao = Text(
            self.window,
            bd=0,
            font = ("regular",28),
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.descricao.place(
            x=330.0,
            y=657.0,
            width=771.0,
            height=176.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1107.0,
            227.0,
            fill="#548AFF",
            outline="")

        self.canvas.create_rectangle(
            -3.0,
            223.99999999999972,
            1107.0,
            227.0,
            fill="#000000",
            outline="")

        #Pegando a imagem do botão imprimir para colocar no background dele
        button_imprimir_image = PhotoImage(
            file=relative_to_assets("button_1.png"))
        
        #Criando o botão de imprimir
        button_imprimir = Button(
            self.window,
            image=button_imprimir_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.imprimirPDF(projeto),
            relief="flat"
        )
        
        button_imprimir.place(
            x=416.0,
            y=874.0,
            width=273.5290832519531,
            height=50.0
        )

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            149.0,
            111.0,
            image=image_image_1
        )

        self.canvas.create_rectangle(
            309.0,
            -3.0,
            312.0,
            227.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            317.0,
            56.0,
            anchor="nw",
            text="Sistema de Gerenciamento de Projetos - SGP",
            fill="#000000",
            font=("Inter SemiBold", 35 * -1)
        )

        self.canvas.create_text(
            510.0,
            141.0,
            anchor="nw",
            text="Informações do Projeto",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            27.0,
            233.0,
            anchor="nw",
            text="ID: ",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            27.0,
            286.0,
            anchor="nw",
            text="Título:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            27.0,
            340.0,
            anchor="nw",
            text="Líder:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            28.0,
            392.0,
            anchor="nw",
            text="Data de entrega:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            27.0,
            445.0,
            anchor="nw",
            text="CPF do cliente:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            27.0,
            657.0,
            anchor="nw",
            text="Descrição geral:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            28.0,
            498.0,
            anchor="nw",
            text="Estado atual:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            27.0,
            551.0,
            anchor="nw",
            text="Tipo de serviço:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            28.0,
            604.0,
            anchor="nw",
            text="Orçamento:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )
        
        #Colocando as informações do projeto na frente dos campos
        
        #Colocando o ID
        self.canvas.create_text(
            82,
            234,
            anchor="nw",
            text = projeto.id,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando o Título
        self.canvas.create_text(
            142,
            286,
            anchor="nw",
            text = projeto.titulo,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando o Líder
        self.canvas.create_text(
            133,
            340,
            anchor="nw",
            text = projeto.lider,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando a Data de entrega
        self.canvas.create_text(
            340,
            392,
            anchor="nw",
            text = projeto.data_entrega,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando a CPF do cliente
        self.canvas.create_text(
            306,
            445,
            anchor="nw",
            text = projeto.cpf_cliente,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando o Estado atual
        self.canvas.create_text(
            271,
            498,
            anchor="nw",
            text = projeto.status,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando o Tipo de serviço
        self.canvas.create_text(
            327,
            551,
            anchor="nw",
            text = projeto.tipo,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando o Orçamento
        self.canvas.create_text(
            255,
            604,
            anchor="nw",
            text = "R$" + str(projeto.orcamento),
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando a Descrição geral
        self.descricao.insert('1.0',projeto.descricao)
        self.descricao.config(state='disabled')
        
        self.window.resizable(False, False)
        
        
        self.window.mainloop()
        
    def imprimirPDF(self,projeto):
        try:
            # Capturar a tela da janela
            x, y, w, h = self.window.winfo_rootx(), self.window.winfo_rooty(), self.window.winfo_width(), self.window.winfo_height()
            imagem = ImageGrab.grab(bbox=(x, y, x+w, y+h))

            file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        
            if file_path:
            
                # Salvar a imagem como PDF
                pdf = canvas.Canvas(file_path, pagesize=(w, h))
                pdf.drawInlineImage(imagem, 0, 0, width=w, height=h)
                pdf.save()
                messagebox.showinfo("PDF Salvo", f"PDF salvo com sucesso em: {file_path}")
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar o PDF: {e}")

