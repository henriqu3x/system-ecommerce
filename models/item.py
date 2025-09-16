from models.compra import Compra
from models.produto import Produto

class Item():
    def __init__(self, id, compra:Compra, produto:Produto, quantidade, preco_unitario):
        self.id = id
        self.compra = compra
        self.produto = produto
        self.quantidade_item = quantidade
        self.preco_unitario_item = preco_unitario