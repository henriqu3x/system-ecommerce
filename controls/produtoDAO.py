from db.connection import Connection
from models.produto import Produto
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class ProdutoDAO(Connection):
    def __init__(self, conexao):
        super().__init__(conexao.user, conexao.password, conexao.host, conexao.port, conexao.database)

    def adicionar(self, produto:Produto):
        if produto:
            try:
                result = self.manipular('''
    insert into produto (nome_pro, categoria_pro, estoque_pro, preco_unitario_pro) values
                                        (%s, %s, %s, %s)
''', (produto.nome, produto.categoria, produto.estoque, produto.preco_unitario))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao tentar adicionar produto: {e}, arquivo: produtoDAO')
                self.desconectar()
                return False
        else:
            logging.error('Nenhum produto inserido para ser adicionado, arquivo: produtoDAO')
            return False

    def ver_produtos(self):
        try:
            dadosBrutos = self.consultar('''
    select id_produto, nome_pro, categoria_pro, estoque_pro, preco_unitario_pro from produto
''')
            
            produtos = []

            for dado in dadosBrutos:
                produto = Produto(dado[0], dado[1], dado[2], dado[3], dado[4])
                produtos.append(produto)
            
            return produtos
        except Exception as e:
            logging.error(f'Falha ao visualizar produtos {e}, arquivo: produtoDAO')
            self.desconectar()
            return []

    def atualizar(self, produto:Produto):
        if produto:
            try:
                result = self.manipular('''
    update produto set nome_pro = %s, categoria_pro = %s, estoque_pro = %s, preco_unitario_pro = %s where id_produto = %s
''', (produto.nome, produto.categoria, produto.estoque, produto.preco_unitario, produto.id))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao atualizar produto: {e}, arquivo: produtoDAO')
                self.desconectar()
                return False
        else:
            logging.error('Nenhum produto inserido ao tentar atualizar, arquivo produtoDAO')
            return False

    def remover(self, produto:Produto):
        if produto:
            try:
                result = self.manipular('delete from produto where id_produto = %s', (produto.id, ))

                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao tentar remover produto: {e}, arquivo: produtoDAO')
                self.desconectar()
                return False
        else:
            logging.error('Nenhum produto inserido para a tentativa de remoção, arquivo: produtoDAO')
            return False