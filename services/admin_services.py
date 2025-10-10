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

    def ver_produtos(self):
        produtos = back_produto.ver_produtos()

        if produtos:
            return produtos
        else:
            return []

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

    def atualizar_preco_produto(self, idProduto, novoPreco):
        produtos = self.ver_produtos()
        produto_selecionado = None

        for produto in produtos:
            if produto.id == idProduto:
                produto_selecionado = produto
                break

        try:
            preco_decimal = float(novoPreco)

            if isinstance(preco_decimal, float):
                produto_selecionado.preco_unitario = preco_decimal
                result = back_produto.atualizar(produto_selecionado)

                if result:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            logging.error(f'falha ao tentar converter valor do preço para decimal, {e}')
            return False
        
    def atualizar_produto(self, idProduto, nome, categoria, estoque, preco):
        produtos = self.ver_produtos()
        produto_selecionado = None

        if produtos:
            for produto in produtos:
                if produto.id == idProduto:
                    produto_selecionado = produto
                    break
                    
            try:
                produto_selecionado.nome = nome or produto_selecionado.nome
                produto_selecionado.categoria = categoria or produto_selecionado.categoria
                produto_selecionado.estoque = estoque or produto_selecionado.estoque
                produto_selecionado.preco_unitario = preco or produto_selecionado.preco_unitario

                estoque_int = int(produto_selecionado.estoque)
                preco_decimal = float(produto_selecionado.preco_unitario)

                if isinstance(preco_decimal, float) and isinstance(estoque_int, int):

                    result = back_produto.atualizar(produto_selecionado)

                    if result:
                        return True
                    else:
                        return False
                else:
                    return False
            except Exception as e:
                logging.error(f'Erro ao atualizar produto {e}')
                return False
        else:
            return False
        
    def remover_produto(self, idProduto):
        produtos = self.ver_produtos()
        produto_selecionado = None

        try:
            id_int = int(idProduto)

            if isinstance(id_int, int):
                for produto in produtos:
                    if produto.id == idProduto:
                        produto_selecionado = produto
                        break

                result = back_produto.remover(produto_selecionado)

                if result:
                    return True
                else:
                    return False
            else:
                return False

        except Exception as e:
            logging.error(f'Falha ao remover produto {e}')
            return False

        result = back_produto.remover()