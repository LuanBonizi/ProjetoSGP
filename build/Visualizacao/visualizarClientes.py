from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, messagebox
from Backend.DataBase import Connection
from Impressao.imprimeCliente import ImprimeCliente
import tkinter as tk
from Cadastro.cadastroCliente import CadastroCliente

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / Path("assets/visualizacaoCliente")


class VisualizarClientes:
    
    def __init__(self,tk_root):
        self.frame = Frame(tk_root,width=1107,height=949)
        self.root = tk_root

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
            370.0,
            7.0,
            anchor="nw",
            text="Clientes do sistema",
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
            command=lambda: self.imprimirCliente(),
            relief="flat"
        )
        
        self.button_visualizar.place(
            x=576.0,
            y=880.0,
            width=273.5290832519531,
            height=50.0
        )
        '''
        self.button_visualizar.place(
            x=463.0,
            y=150.0,
            width=273.5290832519531,
            height=50.0
        )'''

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_atualizar = Button(
            self.frame,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.atualizarDadosCliente(),
            relief="flat"
        )
        self.button_atualizar.place(
            x=263.0,
            y=880.0,
            width=273.5290832519531,
            height=50.0
        )
        '''
        self.button_atualizar.place(
            x=756.0,
            y=150.0,
            width=273.5290832519531,
            height=50.0
        )'''
        
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
        
        self.entrada_filtro.insert(0,"Filtrar clientes pelo nome")
        
        self.button_filtrar = Button(
            self.frame,
            font= ('Arial',20),
            text="Filtrar",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.filtrarClientes(),
            relief="flat"
        )
        
        self.button_filtrar.place(
            x=554,
            y=80,
            width=193.5290832519531,
            height=50.0
        )
        
        self.listaDeClientes = tk.Listbox(
            self.frame,
            font = ('arial',18)
        )
        
        self.listaDeClientes.place(x=83, y=139, width=947, height=696)
        self.listarClientes()
        
    def listarClientes(self):
        conn = Connection()
        clientes = conn.listaClientes()
        
        if len(clientes) == 0:
            self.listaDeClientes.insert(tk.END,"Não há clientes cadastrados")
        
        else:
            for cliente in clientes: 
                info = "CPF: " + str(cliente.cpf_cliente) + " - " + cliente.nome + " - CEL: " + cliente.celular
                    
                self.listaDeClientes.insert(tk.END,info)
            
        conn.desconecta()

    def atualizarDadosCliente(self):
        conn = Connection()
        indice = self.listaDeClientes.curselection()

        info = self.listaDeClientes.get(indice)
        cpf = info[5:19] #Onde está localizado o cpf na string (posição 5 à posição 19)
        cliente = conn.pesquisaCliente(cpf)
        
        opcao = messagebox.askyesno("Confirmação","Você realmente deseja atualizar as informações de " + cliente.nome + " ?")
        
        if opcao == True:
            frame_atualiza_cliente = CadastroCliente(self.root,cliente)
        
    def filtrarClientes(self):
        conn = Connection()
        nome = self.entrada_filtro.get()
        
        clientes_filtrados = conn.buscaClientesPeloNome(nome)
        
        self.listaDeClientes.delete(0, tk.END)
        
        if len(clientes_filtrados) == 0:
            self.listaDeClientes.insert(tk.END,"Não há clientes com esse nome ou algo parecido")
        
        else:
            for cliente in clientes_filtrados: 
                info = "CPF: " + str(cliente.cpf_cliente) + " - " + cliente.nome + " - CEL: " + cliente.celular
                    
                self.listaDeClientes.insert(tk.END,info)
            
        conn.desconecta()
        
    def imprimirCliente(self):
        conn = Connection()
        indice = self.listaDeClientes.curselection()

        info = self.listaDeClientes.get(indice)
        cpf = info[5:19] #Onde está localizado o cpf na string (posição 5 à posição 19)
        cliente = conn.pesquisaCliente(cpf)

        janelaImpressao = ImprimeCliente(cliente)
        
    def relative_to_assets(self,path: str):
        return ASSETS_PATH / Path(path)