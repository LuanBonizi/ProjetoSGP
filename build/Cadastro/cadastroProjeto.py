
from pathlib import Path

from tkinter import *
from tkinter import messagebox

from tkcalendar import *
from datetime import datetime
from Backend.DataBase import Connection


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH.parent / Path("assets/cadastroProjeto")


class CadastroProjeto:
    
    def __init__(self, tk_root):
        
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
            105.0,
            118.0,
            anchor="nw",
            text="Título: ",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            635.0,
            118.0,
            anchor="nw",
            text="Líder:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            105.0,
            266.0,
            anchor="nw",
            text="Data de entrega:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            105.0,
            418.0,
            anchor="nw",
            text="CPF do cliente:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            635.0,
            419.0,
            anchor="nw",
            text="Tipo de serviço:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            327.0,
            562.0,
            anchor="nw",
            text="Descrição geral: ",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            635.0,
            266.0,
            anchor="nw",
            text="Orçamento em R$:",
            fill="#000000",
            font=("Inter", 30 * -1)
        )

        self.canvas.create_text(
            385.0,
            7.0,
            anchor="nw",
            text="Cadastro de Projeto",
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

        #Imagem da entrada de título
        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            311.18890380859375,
            183.0,
            image=self.entry_image_1
        )
        
        self.entrada_titulo = Entry(
            self.frame,
            font= ('Arial',20),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entrada_titulo.place(
            x=109.01522827148438,
            y=154.0,
            width=404.34735107421875,
            height=56.0
        )
        
        
        #Imagem da entrada da data de entrega
        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            311.18890380859375,
            333.0,
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
            x=109.01522827148438,
            y=304.0,
            width=404.34735107421875,
            height=56.0
        )
        
        self.entrada_data.insert(0,"dd/mm/yyyy")
        self.entrada_data.bind("<FocusIn>",self.pegar_data)
        
        #Imagem da entrada do CPF do cliente
        self.entry_image_3 = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            311.18890380859375,
            483.0,
            image=self.entry_image_3
        )
        
        self.cpf_var = StringVar()
                
        self.entrada_cpf = Entry(
            self.frame,
            font= ('Arial',20),
            textvariable=self.cpf_var,
            bd=0,
            validate="key",
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            validatecommand=(self.validacao_numero, "%P")
        )
        self.entrada_cpf.place(
            x=109.01522827148438,
            y=454.0,
            width=404.34735107421875,
            height=56.0
        )
        
        self.entrada_cpf.bind("<KeyRelease>", self.formatar_cpf)

        #Imagem da entrada da descrição geral
        self.entry_image_4 = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            584.7179870605469,
            719.0,
            image=self.entry_image_4
        )
        self.entrada_descricao = Text(
            self.frame,
            font= ('Arial',15),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entrada_descricao.place(
            x=330.018798828125,
            y=598.0,
            width=509.39837646484375,
            height=240.0
        )

        #Imagem da entrada do tipo de serviço
        self.entry_image_5 = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            839.4172058105469,
            482.0,
            image=self.entry_image_5
        )
        self.entrada_tipo = Entry(
            self.frame,
            font= ('Arial',20),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entrada_tipo.place(
            x=637.2435302734375,
            y=453.0,
            width=404.34735107421875,
            height=56.0
        )

        #Imagem da entrada do orçamento
        self.entry_image_6 = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(
            839.4172058105469,
            327.0,
            image=self.entry_image_6
        )
        
        self.orcamento = StringVar()
        
        self.entrada_orcamento = Entry(
            self.frame,
            font= ('Arial',20),
            textvariable=self.orcamento,
            validate="key",
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0,
            validatecommand=(self.validacao_numero, "%P")
        )
        self.entrada_orcamento.place(
            x=637.2435302734375,
            y=298.0,
            width=404.34735107421875,
            height=56.0
        )

        #Imagem da entrada do líder
        self.entry_image_7 = PhotoImage(
            file=self.relative_to_assets("entry_7.png"))
        entry_bg_7 = self.canvas.create_image(
            839.4172058105469,
            183.0,
            image=self.entry_image_7
        )
        self.entrada_lider = Entry(
            self.frame,
            font= ('Arial',20),
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entrada_lider.place(
            x=637.2435302734375,
            y=154.0,
            width=404.34735107421875,
            height=56.0
        )

        #Imagem do botão de cadastrar
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        
        self.button_cadastrar = Button(
            self.frame,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.salvarProjeto(),
            relief="flat"
        )
        
        
        self.button_cadastrar.place(
            x=447.9534606933594,
            y=880.0,
            width=273.5290832519531,
            height=50.0
        )

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
    def salvarProjeto(self):
        conn = Connection()
        titulo = self.entrada_titulo.get()
        data_entrega = self.entrada_data.get()
        cpf_cliente = self.entrada_cpf.get()
        lider = self.entrada_lider.get()
        orcamento = self.entrada_orcamento.get()
        tipo = self.entrada_tipo.get()
        descricao = self.entrada_descricao.get('1.0',END)
        
        #Variáveis para a verificação
        cliente = conn.pesquisaCliente(cpf_cliente)
        if data_entrega != "dd/mm/yyyy":
            data_escolhida = datetime.strptime(data_entrega, "%d/%m/%Y").date()
        else:
            data_escolhida = datetime.now().date()
            
        data_atual = datetime.now().date()
        
        
        
        if titulo == "":
            messagebox.showerror("Erro", "Preencha o título corretamente corretamente!")
            
        elif lider == "" or orcamento == "" or tipo == "":
            messagebox.showerror("Erro", "Preencha as informações de líder, orçamento e tipo corretamente!")
        
        elif len(cpf_cliente) != 14:
            messagebox.showerror("Erro", "Preencha o CPF corretamente!")
            
        elif data_entrega == "dd/mm/yyyy" or data_atual >= data_escolhida:
            messagebox.showerror("Erro", "Escolha uma data adequada!")
        
        #Pega do texto da entrada do tipo Text e remove os espaços em branco, depois verifica se há alguma coisa
        elif not(self.entrada_descricao.get('1.0',END).strip()):
            messagebox.showerror("Erro", "Coloque pelo menos uma descrição mínima!")
        
        #Caso em que não há um cliente com o cpf fornecido no banco
        elif cliente == None:
            messagebox.showerror("Erro", "Esse cliente não está cadastrado!")
            
        else:
            conn.insereProjeto(titulo,lider,data_entrega,descricao,orcamento,cpf_cliente,tipo,'Em andamento')
            messagebox.showinfo("Sucesso!","O projeto foi cadastrado!")
            
            #Deleta as informações de todos as entradas do Frame
            for widget in self.frame.winfo_children():
                if isinstance(widget, Entry):
                    widget.delete(0, "end")
            self.entrada_descricao.delete('1.0',END)
            conn.desconecta() # fecha a conecão com o banco
            
    def relative_to_assets(self,path: str):
        return ASSETS_PATH / Path(path)