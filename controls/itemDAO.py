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

    def ver_itens(self, compra:Compra):
        try:
            dadosBrutos = self.consultar('''
            SELECT 
                item.id_item,              
                item.compra_id,            
                item.produto_id,           
                item.quantidade_ite,       
                item.preco_unitario_ite,   
                produto.id_produto,        
                produto.nome_pro,          
                produto.categoria_pro,     
                produto.estoque_pro,       
                produto.preco_unitario_pro,
                compra.preco_total_com,    
                compra.status_com          
            FROM item
            INNER JOIN produto ON item.produto_id = produto.id_produto
            INNER JOIN compra ON item.compra_id = compra.id_compra  
            WHERE item.compra_id = %s
        ''', (compra.id, ))

            items = []

            for dado in dadosBrutos:
                ID_ITEM = 0
                ID_COMPRA = 1
                QUANTIDADE = 3
                PRECO_UNITARIO = 4
                
                ID_PRODUTO = 5
                NOME_PRO = 6
                CATEGORIA_PRO = 7
                ESTOQUE_PRO = 8
                PRECO_PRO = 9
                
                PRECO_TOTAL_COMPRA = 10 
                STATUS_COMPRA = 11     
                
                item = Item(
                    dado[ID_ITEM],
                    Compra(
                        dado[ID_COMPRA], 
                        None,                       
                        dado[PRECO_TOTAL_COMPRA],   
                        None,                       
                        dado[STATUS_COMPRA]       
                    ),
                    Produto(
                        dado[ID_PRODUTO], dado[NOME_PRO], dado[CATEGORIA_PRO], dado[ESTOQUE_PRO], dado[PRECO_PRO]
                    ),
                    dado[QUANTIDADE],
                    dado[PRECO_UNITARIO]
                )
                items.append(item)

            return items
        except Exception as e:
            logging.error(f'Falha ao visualizar items {e}, arquivo: itemDAO')
            self.desconectar()
            return []


    def atualizar_item_simples(self, item:Item):
        if item:
            try:
                result = self.manipular('''
                    UPDATE item set quantidade_ite = %s, preco_unitario_ite = %s where id_item = %s
                ''', (item.quantidade, item.preco_unitario, item.id))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao atualizar item (simples): {e}, arquivo: itemDAO')
                self.desconectar()
                return False
        else:
            return False
        
    def finalizar_compra_transacional(self, item:Item): 
        if item:
            try:
                result_produto = self.manipular('''
                    UPDATE produto SET estoque_pro = %s WHERE id_produto = %s
                ''', (item.produto.estoque, item.produto.id))

                result_compra = self.manipular('''
                    UPDATE compra SET status_com = %s, preco_total_com = %s WHERE id_compra = %s
                ''', (item.compra.status, item.compra.preco_total, item.compra.id))
                
                result_item = self.manipular('''
                    UPDATE item set quantidade_ite = %s, preco_unitario_ite = %s where id_item = %s
                ''', (item.quantidade, item.preco_unitario, item.id))
                
                if result_produto and result_compra and result_item:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha na transação ao finalizar compra: {e}, arquivo: itemDAO')
                self.desconectar()
                return False
        else:
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