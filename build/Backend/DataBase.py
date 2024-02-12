import os
import sqlite3
from .objetos import *

class Connection:
    
    def __init__(self):
        caminho_absoluto = os.path.abspath(os.path.dirname(__file__))

        caminho_banco_dados = os.path.join(caminho_absoluto, 'SGB.db')
        
        self.conn = sqlite3.connect(caminho_banco_dados)
        
        self.cursor = self.conn.cursor()
    
    #Função para inicializar o banco de dados
    def criaBanco(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Projetos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo varchar(60) NOT NULL,
                lider varchar(30) NOT NULL,
                tipo varchar(30) NOT NULL,
                data_entrega DATE NOT NULL,
                descricao varchar(300) NOT NULL,
                orcamento float(24) NOT NULL,
                cpf_cliente varchar(17),
                status varchar(15),
                FOREIGN KEY (cpf_cliente) REFERENCES Clientes(cpf_cliente))''')
    
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Clientes(
                cpf_cliente varchar(17) PRIMARY KEY,
                nome varchar(30) NOT NULL,
                data_nascimento DATE NOT NULL,
                telefone varchar(20) NOT NULL,
                email varchar(30) NOT NULL)''')
        self.conn.commit()
        self.conn.close()

    #################### FUNÇÕES RELACIONADAS AOS PROJETOS E SUAS OPERAÇÕES NO BANCO ####################
    def insereProjeto(self, titulo, lider, data_entrega, descricao, orcamento, cpf_cliente, tipo, status):
        values = (titulo, lider, tipo, data_entrega, descricao, orcamento, cpf_cliente, status)
        insert_script = 'INSERT INTO Projetos (titulo, lider, tipo, data_entrega, descricao, orcamento, cpf_cliente, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        self.cursor.execute(insert_script, values)
        self.conn.commit()
    
    def pesquisaProjeto(self, id):
        insert_script = 'SELECT * FROM Projetos WHERE id = ?'
        self.cursor.execute(insert_script, (id,))
        
        resultado = None
        resultado = self.cursor.fetchone()
        
        if resultado is not None:
            projeto = Projeto(resultado[0],resultado[1],resultado[2],resultado[3],resultado[4],resultado[5], resultado[6],resultado[7],resultado[8])
            return projeto
        else:
            return resultado
        
    def listaProjetos(self):
        insert_script = 'SELECT * FROM Projetos'
        self.cursor.execute(insert_script)
        projetos = []
        for results in self.cursor.fetchall():
            projetos.append(Projeto(results[0],results[1],results[2],results[3],results[4],results[5], results[6], results[7],results[8]))
        
        return projetos
    
    def atualizaProjeto(self,id, status):
        update_script = 'UPDATE Projetos SET status = ? WHERE id = ?'
        self.cursor.execute(update_script,(status,id))
        self.conn.commit()
    
    def buscaProjetosPeloTitulo(self, titulo):
        select_script = 'SELECT * FROM Projetos WHERE titulo LIKE ?'
        self.cursor.execute(select_script,(f'%{titulo}%',))
        
        projetos_filtrados = []
        for results in self.cursor.fetchall():
            projetos_filtrados.append(Projeto(results[0],results[1],results[2],results[3],results[4],results[5], results[6], results[7],results[8]))
        
        return projetos_filtrados
        
    def buscaProjetosComMaiorPrioridade(self):
        select_script = 'SELECT * FROM projetos ORDER BY data_entrega ASC'
        self.cursor.execute(select_script)
        projetos = []
        i = 0
        
        for results in self.cursor.fetchall():
            if i < 10 and results[8] == 'Em andamento':
                projetos.append(Projeto(results[0],results[1],results[2],results[3],results[4],results[5], results[6], results[7],results[8]))
                i = i + 1
            elif i == 10:
                break
        
        return projetos
    
    #################### FUNÇÕES RELACIONADAS AOS CLIENTES E SUAS OPERAÇÕES NO BANCO ####################
    def insereCliente(self,cpf_cliente,nome,data_nascimento,celular,email):
        values = (cpf_cliente,nome,data_nascimento,celular,email)
        insert_script = 'INSERT INTO Clientes (cpf_cliente,nome,data_nascimento,telefone,email) VALUES (?, ?, ?, ?, ?)'
        self.cursor.execute(insert_script, values)
        self.conn.commit()
    
    def pesquisaCliente(self,cpf_cliente):
        insert_script = 'SELECT * FROM Clientes WHERE cpf_cliente = ?'
        self.cursor.execute(insert_script, (cpf_cliente,))
        
        resultado = None
        
        resultado = self.cursor.fetchone()
        
        if resultado is not None:
            cliente = Cliente(resultado[0],resultado[1],resultado[2],resultado[3],resultado[4])
            return cliente
        else:
            return resultado
        
    
    def listaClientes(self):
        insert_script = 'SELECT * FROM Clientes'
        self.cursor.execute(insert_script)
        clientes = []
        
        for results in self.cursor.fetchall():
            clientes.append(Cliente(results[0],results[1],results[2],results[3],results[4]))
        
        return clientes
    
    def atualizaCliente(self,cpf, nome, data_nascimento,telefone,email):
        update_script = 'UPDATE Clientes SET nome = ?, data_nascimento = ?, telefone = ?, email = ?  WHERE cpf_cliente = ?'
        self.cursor.execute(update_script,(nome,data_nascimento,telefone,email, cpf))
        self.conn.commit()
        
    def buscaClientesPeloNome(self,nome):
        select_script = "SELECT * FROM Clientes WHERE nome LIKE ?"
        self.cursor.execute(select_script,(f'%{nome}%',))
        
        clientes_filtrados = []
        
        for results in self.cursor.fetchall():
            clientes_filtrados.append(Cliente(results[0],results[1],results[2],results[3],results[4]))
        
        return clientes_filtrados
        
        
    def buscaProjetosCliente(self,cpf):
        select_script = 'SELECT titulo FROM projetos WHERE cpf_cliente = ?'
        self.cursor.execute(select_script,(cpf,))
        titulos = []
        for results in self.cursor.fetchall():
            titulos.append(results[0])
            
        return titulos
    
    #Função que desconecta do banco
    def desconecta(self):
        self.conn.close()