

class Projeto:
    def __init__(self,id,titulo,lider,tipo,data_entrega,descricao, orcamento, cpf_cliente, status):
        self.id = id
        self.titulo = titulo
        self.lider = lider
        self.tipo = tipo
        self.data_entrega = data_entrega
        self.descricao = descricao
        self.orcamento = orcamento
        self.cpf_cliente = cpf_cliente
        self.status = status
        
class Cliente:
    def __init__(self, cpf_cliente, nome, data_nascimento, celular, email):
        self.cpf_cliente = cpf_cliente
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.celular = celular
        self.email = email