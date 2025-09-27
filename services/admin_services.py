from container import back_produto
from models.produto import Produto
import logging

logging.basicConfig(level=logging.DEBUG,  format="%(asctime)s - %(levelname)s - %(message)s")


class AdminServices():
    def __init__(self):
        pass

    def cadastrar_produto(self, nome, categoria, estoque, preco):
        produto = Produto(None, nome, categoria, estoque, preco)

        result = back_produto.adicionar(produto)

        if result:
            return True
        else:
            return False


    def ver_produtos_estoque15(self):
        pass

    def atualizar_estoque_produto(self):
        pass

    def atualizar_preco_produto(self):
        pass

    def atualizar_produto(self):
        pass

    def remover_produto(self):
        pass