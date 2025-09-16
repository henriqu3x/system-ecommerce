import logging
from models.compra import Compra
from models.produto import Produto
from models.item import Item
from db.connection import Connection

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class ItemDAO(Connection):
    def __init__(self, conexao):
        super().__init__(conexao.user, conexao.password, conexao.host, conexao.port, conexao.database)

    def adicionar(self, item:Item):
        if item:
            try:
                result = self.manipular('''
    insert into item (compra_id, produto_id, quantidade_ite, preco_unitario_ite) values
                                        (%s, %s, %s, %s)
''', (item.compra.id, item.produto.id, item.quantidade, item.preco_unitario))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao tentar adicionar item: {e}, arquivo: itemDAO')
                self.desconectar()
                return False
        else:
            logging.error('Nenhum item inserido para ser adicionado, arquivo: itemDAO')
            return False

    def ver_itens(self):
        try:
            dadosBrutos = self.consultar('''
    select id_item, nome_pro, quantidade_ite, preco_unitario_ite from item
                                         inner join produto on produto_id = id_produto
''')
            
            items = []

            for dado in dadosBrutos:
                item = Item(dado[0], Compra(None, None, None, None), Produto(None, dado[1], None, None, None), dado[2], dado[3])
                items.append(item)
            
            return items
        except Exception as e:
            logging.error(f'Falha ao visualizar items {e}, arquivo: itemDAO')
            self.desconectar()
            return []

    def atualizar(self, item:Item):
        if item:
            try:
                result = self.manipular('''
    update item set compra_id = %s, produto_id = %s, quantidade_ite = %s, preco_unitario_ite = %s where id_item = %s
''', (item.compra.id, item.produto.id, item.quantidade, item.preco_unitario, item.id))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao atualizar item: {e}, arquivo: itemDAO')
                self.desconectar()
                return False
        else:
            logging.error('Nenhum item inserido ao tentar atualizar, arquivo itemDAO')
            return False

    def remover(self, item:Item):
        if item:
            try:
                result = self.manipular('delete from item where id_item = %s', (item.id, ))

                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao tentar remover item: {e}, arquivo: itemDAO')
                self.desconectar()
                return False
        else:
            logging.error('Nenhum item inserido para a tentativa de remoção, arquivo: itemDAO')
            return False