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
        produtos = back_produto.ver_produtos()
        produtos_estoque_15 = []

        if produtos:
            for produto in produtos:
                if produto.estoque <= 15:
                    produtos_estoque_15.append(produto)
            return produtos_estoque_15
        else:
            return []

    def atualizar_estoque_produto(self, idProduto, qtdEstoque):
        if idProduto > 0 and qtdEstoque >= 0:
            produtos = self.ver_produtos_estoque15()
            produto_escolhido = None

            for produto in produtos:
                if produto.id == idProduto:
                    produto_escolhido = produto
                    break

            if produto_escolhido == None:
                return False

            produto_escolhido.estoque = qtdEstoque
            result = back_produto.atualizar(produto_escolhido)

            if result:
                return True
            else:
                return False

    def atualizar_preco_produto(self, idProduto):
        pass

    def atualizar_produto(self, idProduto):
        pass

    def remover_produto(self, idProduto):
        pass