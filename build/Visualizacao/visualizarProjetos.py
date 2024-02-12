from pathlib import Path

from tkinter import Canvas, Button, PhotoImage, Frame, messagebox, Entry
import tkinter as tk
from Backend.DataBase import Connection
from Impressao.imprimeProjeto import ImprimeProjeto
from datetime import datetime

import re

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / Path("assets/visualizacaoProjeto")

class VisualizarProjetos:
    
    def __init__(self,tk_root):
        self.frame = Frame(tk_root,width=1107,height=949)

        self.frame.configure(bg = "#FFFFFF")


        self.canvas = Canvas(
            self.frame,
            bg = "#FFFFFF",
            height = 949,
            width = 1107,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.frame.place(x=333,y=75)
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1107.0,
            949.0,
            fill="#98A1F3",
            outline="")

        self.canvas.create_text(
            367.0,
            7.0,
            anchor="nw",
            text="Projetos do sistema",
            fill="#000000",
            font=("Inter", 40 * -1)
        )

        self.canvas.create_rectangle(
            -1.0,
            62.999999999999716,
            1107.0,
            64.0,
            fill="#000000",
            outline="")

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        
        self.button_visualizar = Button(
            self.frame,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.imprimirProjeto(),
            relief="flat"
        )
        self.button_visualizar.place(
            x=576.0,
            y=880.0,
            width=273.5290832519531,
            height=50.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        
        self.button_atualizar = Button(
            self.frame,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.atualizaStatusProjeto(),
            relief="flat"
        )
        self.button_atualizar.place(
            x=263.0,
            y=880.0,
            width=273.5290832519531,
            height=50.0
        )

        self.entrada_filtro = Entry(
            self.frame,
            font= ('Arial',20),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        
        self.entrada_filtro.place(
            x=83,
            y=82,
            width=450,
            height=46
        )
        
        self.entrada_filtro.insert(0,"Filtrar projetos pelo título")
        
        self.button_filtrar = Button(
            self.frame,
            font= ('Arial',20),
            text="Filtrar",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.filtrarProjetos(),
            relief="flat"
        )
        
        self.button_filtrar.place(
            x=554,
            y=80,
            width=193.5290832519531,
            height=50.0
        )
        
        
        self.listaDeProjetos = tk.Listbox(
            self.frame,
            font = ('arial',18)
        )
        
        self.listaDeProjetos.place(x=83, y=139, width=947, height=696)
        self.listarProjetos()
        
    def listarProjetos(self):
        conn = Connection()
        projetos = conn.listaProjetos()
        
        if len(projetos) == 0:
            self.listaDeProjetos.insert(tk.END,"Não há projetos cadastrados")
            
        else:
            for projeto in projetos:
                status = projeto.status
                if status == "Em andamento":
                    data_de_entrega = datetime.strptime(str(projeto.data_entrega), "%d/%m/%Y")

                    data_atual = datetime.now()

                    diferenca_em_dias = (data_de_entrega - data_atual).days
                
                    info = "ID: " + str(projeto.id) + " - " + projeto.titulo + " - " + projeto.lider + " - " + str(diferenca_em_dias) + " dias restantes"
                else:
                    info = "ID: " + str(projeto.id) + " - " + projeto.titulo + " - " + projeto.lider + " - " + status
                    
                self.listaDeProjetos.insert(tk.END,info)
        conn.desconecta()
    
    def atualizaStatusProjeto(self):
        conn = Connection()
        indice = self.listaDeProjetos.curselection()

        info = self.listaDeProjetos.get(indice)
        match = re.search(r'\d+', info)
        id = int(match.group())

        projeto = conn.pesquisaProjeto(id)
        if projeto.status == "Em andamento":
        
            self.janela_status = tk.Toplevel(self.frame)
            self.janela_status.title("Atualizar status")

            label = tk.Label(self.janela_status, text="Para qual status você deseja alterar o projeto ?")
            label.pack(pady=10)

            botao_terminar = tk.Button(self.janela_status, text="Concluído", command=lambda: self.atualizaListaProjetos(id,"Concluído"))
            botao_terminar.pack(side=tk.LEFT, padx=5)

            botao_cancelar = tk.Button(self.janela_status, text="Cancelado", command=lambda: self.atualizaListaProjetos(id,"Cancelado"))
            botao_cancelar.pack(side=tk.RIGHT, padx=5)
        else:
            messagebox.showerror("Erro", "Esse projeto já foi finalizado!")
        
    
    def atualizaListaProjetos(self, id, status):
        conn = Connection()
        conn.atualizaProjeto(id,status)
        self.listaDeProjetos.delete(0,tk.END)
        self.listarProjetos()
        self.janela_status.destroy()
    
    def filtrarProjetos(self):
        conn = Connection()
        titulo = self.entrada_filtro.get()
        projetos_filtrados = conn.buscaProjetosPeloTitulo(titulo) 
        
        #Limpa a lista de projetos
        self.listaDeProjetos.delete(0,tk.END)
        
        if len(projetos_filtrados) == 0:
            self.listaDeProjetos.insert(tk.END,"Não há projetos com esse título ou algo parecido")
            
        else:
            for projeto in projetos_filtrados:
                status = projeto.status
                if status == "Em andamento":
                    data_de_entrega = datetime.strptime(str(projeto.data_entrega), "%d/%m/%Y")

                    data_atual = datetime.now()

                    diferenca_em_dias = (data_de_entrega - data_atual).days
                
                    info = "ID: " + str(projeto.id) + " - " + projeto.titulo + " - " + projeto.lider + " - " + str(diferenca_em_dias) + " dias restantes"
                else:
                    info = "ID: " + str(projeto.id) + " - " + projeto.titulo + " - " + projeto.lider + " - " + status
                    
                self.listaDeProjetos.insert(tk.END,info)
        conn.desconecta()
        
    
    def imprimirProjeto(self):
        conn = Connection()
        indice = self.listaDeProjetos.curselection()

        info = self.listaDeProjetos.get(indice)
        match = re.search(r'\d+', info)
        id = int(match.group())

        projeto = conn.pesquisaProjeto(id)
        JanelaImpressao = ImprimeProjeto(projeto)
    
    def relative_to_assets(self,path: str):
        return ASSETS_PATH / Path(path)
