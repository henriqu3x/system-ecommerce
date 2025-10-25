from models.cliente import Cliente

class Compra():
    def __init__(self, id, cliente:Cliente, preco_total, data_hora, status):
        self.id = id
        self.cliente = cliente
        self.preco_total = preco_total
        self.data_hora = data_hora
        self.status = status