from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label
import tkinter as tk
from time import *
from Backend.DataBase import Connection
from Impressao.imprimeProjeto import ImprimeProjeto
from datetime import datetime
import locale
import re

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / Path("assets/telaInicial")


class TelaInicial:
    
    def __init__(self, tk_root):
        
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
            376.0,
            7.0,
            anchor="nw",
            text="Bem vindo ao SGP!",
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
            x=420.0,
            y=878.0,
            width=273.5290832519531,
            height=50.0
        )

        #Label do relógio
        self.time_label = Label(self.frame,font=("Arial",60),fg='#000000',bg='#98A1F3')
        self.time_label.pack()
        self.time_label.place(x=30,y=184,width=600,height=187)
        
        #Label do dia da semana
        self.day_label = Label(self.frame,font=("Arial",30),fg='#000000',bg='#98A1F3')
        self.day_label.pack()
        self.day_label.place(x=630,y=230,width=330,height=50)
        
        #Label do dia do mês
        self.date_label = Label(self.frame,font=("Arial",30),fg='#000000',bg='#98A1F3')
        self.date_label.pack()
        self.date_label.place(x=630,y=300,width=330,height=50)
        
        
        self.update_time()

        self.canvas.create_text(
            83.0,
            522.0,
            anchor="nw",
            text="Projetos com maior prioridade:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )
        
        self.listaDeProjetos = tk.Listbox(
            self.frame,
            font = ('arial',18)
        )
        
        self.listaDeProjetos.place(x=83, y=558, width=947, height=277)
        
        self.listaProjetosPorPrioridade()
    
    def update_time(self):
        time_string = strftime("%I:%M:%S %p")
        self.time_label.config(text=time_string)
        
        day_string = strftime("%A")
        self.day_label.config(text=day_string)
        
        date_string = strftime("%B %d, %Y")
        self.date_label.config(text=date_string)
        
        self.time_label.after(1000,self.update_time)
    
    def listaProjetosPorPrioridade(self):
        conn = Connection()
        projetos = conn.buscaProjetosComMaiorPrioridade()
        print(len(projetos))
        if len(projetos) == 0:
            self.listaDeProjetos.insert(tk.END,"Não há projetos em andamento!")
            
        else:
            for projeto in projetos:
                status = projeto.status
                
                data_de_entrega = datetime.strptime(str(projeto.data_entrega), "%d/%m/%Y")

                data_atual = datetime.now()

                diferenca_em_dias = (data_de_entrega - data_atual).days
                
                info = "ID: " + str(projeto.id) + " - " + projeto.titulo + " - " + projeto.lider + " - " + str(diferenca_em_dias) + " dias restantes"
                
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
        
        conn.desconecta()
        
    def relative_to_assets(self,path: str):
        return ASSETS_PATH / Path(path)
