from pathlib import Path

from tkinter import *
from tkinter import messagebox

from tkcalendar import *
from email_validator import validate_email
from datetime import datetime
from Backend.DataBase import Connection


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / Path("assets/cadastroCliente")


class CadastroCliente:
    def __init__(self,tk_root, cliente):
        
        self.frame = Frame(tk_root,width=1107,height=949)

        
        self.frame.configure(bg = "#FFFFFF")

        #Registra a validação baseada na função validar_entrada_numero
        self.validacao_numero = self.frame.register(self.validar_entrada_numero)

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
            347.0,
            118.0,
            anchor="nw",
            text="Nome:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            354.0,
            262.0,
            anchor="nw",
            text="Data de nascimento:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            352.0,
            406.0,
            anchor="nw",
            text="CPF do cliente:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            355.0,
            550.0,
            anchor="nw",
            text="Telefone:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            355.0,
            694.0,
            anchor="nw",
            text="E-mail:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_rectangle(
            -1.0,
            62.999999999999716,
            1107.0,
            64.0,
            fill="#000000",
            outline="")

        #Imagem da entrada do nome
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            554.1736755371094,
            183.0,
            image=self.entry_image_1
        )
        
        self.entrada_nome = Entry(
            self.frame,
            font= ('Arial',20),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entrada_nome.place(
            x=352.0,
            y=154.0,
            width=404.34735107421875,
            height=56.0
        )

        #Imagem da entrada da data de nascimento
        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            557.1736755371094,
            327.0,
            image=self.entry_image_2
        )
        self.entrada_data = Entry(
            self.frame,
            font= ('Arial',20),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entrada_data.place(
            x=355.0,
            y=298.0,
            width=404.34735107421875,
            height=56.0
        )
        
        self.entrada_data.bind("<FocusIn>",self.pegar_data)

        #Imagem da entrada do CPF
        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            557.1736755371094,
            471.0,
            image=self.entry_image_3
        )
        
        self.cpf_var = StringVar()
        
        self.entrada_cpf = Entry(
            self.frame,
            font= ('Arial',20),
            textvariable=self.cpf_var,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
        )
        self.entrada_cpf.place(
            x=355.0,
            y=442.0,
            width=404.34735107421875,
            height=56.0
        )

        self.entrada_cpf.bind("<KeyRelease>", self.formatar_cpf)
        
        #Imagem da entrada do telefone 
        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            557.1736755371094,
            615.0,
            image=self.entry_image_4
        )
        self.entrada_telefone = Entry(
            self.frame,
            font= ('Arial',20),
            validate="key",
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            validatecommand=(self.validacao_numero, "%P")
        )
        self.entrada_telefone.place(
            x=355.0,
            y=586.0,
            width=404.34735107421875,
            height=56.0
        )


        #Imagem da entrada do e-mail
        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            557.1736755371094,
            759.0,
            image=self.entry_image_5
        )
        self.entrada_email = Entry(
            self.frame,
            font= ('Arial',20),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        
        
        self.entrada_email.place(
            x=355.0,
            y=730.0,
            width=404.34735107421875,
            height=56.0
        )
        
        #Verifica se é um cadastro de um novo cliente ou uma atualização dos dados
        if cliente == None:
            
            self.canvas.create_text(
            361.0,
            7.0,
            anchor="nw",
            text="Cadastro de Cliente",
            fill="#000000",
            font=("Inter", 40 * -1)
        )
            
            self.entrada_data.insert(0,"dd/mm/yyyy")
            self.button_image_1 = PhotoImage(
                file=self.relative_to_assets("button_1.png"))
            self.button_cadastrar = Button(
                self.frame,
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.salvarCliente("Cadastro"),
                relief="flat"
            )
            
            self.button_cadastrar.place(
                x=420.0,
                y=878.0,
                width=273.5290832519531,
                height=50.0
            )
        
        #Caso da atualização
        else:
            self.canvas.create_text(
            340.0,
            7.0,
            anchor="nw",
            text="Atualização de Cliente",
            fill="#000000",
            font=("Inter", 40 * -1)
        )
            
            self.button_image_1 = PhotoImage(
                file=self.relative_to_assets("button_2.png"))
            self.button_atualizar = Button(
                self.frame,
                image=self.button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: self.salvarCliente("Atualização"),
                relief="flat"
            )
            
            
            self.button_atualizar.place(
                x=420.0,
                y=878.0,
                width=273.5290832519531,
                height=50.0
            )
            
            self.entrada_cpf.insert(0,cliente.cpf_cliente)
            self.entrada_cpf.config(state='disabled')
            
            self.entrada_data.insert(0,cliente.data_nascimento)
            self.entrada_email.insert(0,cliente.email)
            self.entrada_nome.insert(0,cliente.nome)
            self.entrada_telefone.insert(0,cliente.celular)
        
    #################### FUNÇÕES PARA LIDAR COM A ENTRADA DA DATA E CRIAÇÃO DO CALENDÁRIO ####################
    def pegar_data(self,event):
        self.date_window = Toplevel()
        self.date_window.title("Escolha uma data")
        self.date_window.geometry("250x250")
        
        self.calendar = Calendar(self.date_window, selectmode='day', date_pattern="dd/mm/yyyy")
        self.calendar.pack(padx=10, pady=10)
        
        self.button_selecionar = Button(self.date_window,text="Selecionar",command=self.selecionar_data)
        self.button_selecionar.place(x=80,y=190)
        
    def selecionar_data(self):
        self.entrada_data.delete(0,'end')
        self.entrada_data.insert(0,self.calendar.get_date())
        self.date_window.destroy()
        self.frame.focus_set()
        
    #################### FUNÇÕES PARA LIDAR COM A ENTRADA DO CPF ####################
    def validar_entrada_numero(self, valor):
        # Função de validação para aceitar apenas números
        return valor.isdigit() or valor == ""
    
    def formatar_cpf(self, event):
        # Função para formatar o CPF (###.###.###-##)
        cpf = self.entrada_cpf.get()
        cpf_formatado = self.formatar_cpf_texto(cpf)
        self.cpf_var.set(cpf_formatado)
    
    def formatar_cpf_texto(self, cpf):
        # Função para formatar o CPF (###.###.###-##)
        cpf = ''.join(c for c in cpf if c.isdigit())  # Remover caracteres não numéricos
        if len(cpf) > 6:
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        elif len(cpf) > 3:
            cpf = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:]}"
        elif len(cpf) > 0:
            cpf = f"{cpf[:3]}.{cpf[3:]}"
        return cpf
        
     #################### FUNÇÃO PARA SALVAR O PROJETO NO BANCO DE DADOS ####################
    def salvarCliente(self, flag):
        conn = Connection()
        nome = self.entrada_nome.get()
        data_nascimento = self.entrada_data.get()
        cpf = self.entrada_cpf.get()
        telefone = self.entrada_telefone.get()
        email = self.entrada_email.get()
        
        #Varriáveis para validação
        cliente = conn.pesquisaCliente(cpf)
        if data_nascimento != "dd/mm/yyyy":
            data_selecionada = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
        else:
            data_selecionada = datetime.now().date()
            
        data_atual = datetime.now().date()
        
        try:
            validate_email(email)
              
            if nome == "" or data_nascimento == "dd/mm/yyyy":
                messagebox.showerror("Erro", "Preencha as informações de nome e data de nascimento corretamente!")
            
            elif (data_atual - data_selecionada).days < 365*18:
                messagebox.showerror("Erro", "O cliente deve ter no mínimo 18 anos!")
                
            elif telefone == "" or len(telefone) !=11:
                messagebox.showerror("Erro", "Preencha o telefone corretamente!")
            
            elif len(cpf) != 14:
                print(len(cpf))
                messagebox.showerror("Erro", "Preencha o CPF corretamente!")
            
            elif cliente != None and flag == "Cadastro":
                messagebox.showerror("Erro", "Esse cliente já está cadastrado!")
            
            else:
                
                if flag == "Cadastro":
                    conn.insereCliente(cpf,nome,data_nascimento,telefone,email)
                    messagebox.showinfo("Sucesso!","O cliente foi cadastrado!")
                    
                    #Deleta as informações de todos as entradas do Frame
                    for widget in self.frame.winfo_children():
                        if isinstance(widget, Entry):
                            widget.delete(0, "end")
                else:
                    conn.atualizaCliente(cpf,nome,data_nascimento,telefone,email)
                    messagebox.showinfo("Sucesso!", "As informações foram atualizadas!")
                    self.frame.destroy()
                        
                conn.desconecta() # fecha a conecão com o banco
        except Exception as e:
            messagebox.showerror("Erro", "E-mail inválido!")
            print(e)
        
    def relative_to_assets(self,path: str):
        return ASSETS_PATH / Path(path)
