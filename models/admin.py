from models.usuario import Usuario

class Admin():
    def __init__(self, id, usuario:Usuario, nome, telefone, endereco):
        self.id = id
        self.usuario = usuario
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco