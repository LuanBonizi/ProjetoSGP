from pathlib import Path
from tkinter import *
from tkinter import filedialog, messagebox

from PIL import ImageGrab
from datetime import datetime
from Backend.DataBase import Connection
from reportlab.pdfgen import canvas


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / Path("assets/impressaoCliente")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ImprimeCliente:
    
    def __init__(self, cliente):
        self.window = Toplevel()

        self.window.title("Impressão de Cliente")

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

        button_imprimir_image = PhotoImage(
            file=relative_to_assets("button_1.png"))
        
        self.button_imprimir = Button(
            self.window,
            image=button_imprimir_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.imprimirPDF(),
            relief="flat"
        )

        self.button_imprimir.place(
            x=416.0,
            y=874.0,
            width=273.5290832519531,
            height=50.0
        )

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            158.0,
            116.0,
            image=self.image_image_1
        )

        self.canvas.create_rectangle(
            309.0,
            -3.0,
            312.0,
            227.0,
            fill="#000000",
            outline="")

        self.canvas.create_text(
            321.0,
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
            text="Informações do Cliente",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            36.0,
            265.0,
            anchor="nw",
            text="Nome:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            36.0,
            318.0,
            anchor="nw",
            text="CPF:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            36.0,
            371.0,
            anchor="nw",
            text="Data de Nascimento:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            36.0,
            424.0,
            anchor="nw",
            text="Telefone:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            36.0,
            477.0,
            anchor="nw",
            text="E-mail:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.canvas.create_text(
            36.0,
            612.0,
            anchor="nw",
            text="Projetos solicitados:",
            fill="#000000",
            font=("Inter SemiBold", 36 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            741.5,
            736.0,
            image=self.entry_image_1
        )
        self.projetos_solicitados = Text(
            self.window,
            font = ('regular',28),
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.projetos_solicitados.place(
            x=398.0,
            y=610.0,
            width=687.0,
            height=226.0
        )
        
        #Colocando as informações do cliente na frente dos campos
        
        #Colocando o nome
        self.canvas.create_text(
            163,
            265,
            anchor="nw",
            text = cliente.nome,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando o CPF
        self.canvas.create_text(
            134,
            318,
            anchor="nw",
            text = cliente.cpf_cliente,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando o data de nascimento
        self.canvas.create_text(
            410,
            371,
            anchor="nw",
            text = cliente.data_nascimento,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando o telefone
        self.canvas.create_text(
            210,
            424,
            anchor="nw",
            text = cliente.celular,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        
        #Colocando o e-mail
        self.canvas.create_text(
            174,
            477,
            anchor="nw",
            text = cliente.email,
            fill="#000000",
            font=("regular", 36 * -1)
        )
        #Colocando os projetos solicitados
        conn = Connection()
        projetos = conn.buscaProjetosCliente(cliente.cpf_cliente)
        string_formatada = ""

        for i in range(0,len(projetos)):
            if i < len(projetos) - 1:
                string_formatada += projetos[i] + ', '
            else:
                string_formatada += projetos[i] + '.'
            print(i)
        
        self.projetos_solicitados.insert('1.0',string_formatada)
        self.projetos_solicitados.config(state='disabled')
        
        
        self.window.resizable(False, False)
        self.window.mainloop()
        
    def imprimirPDF(self):
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
