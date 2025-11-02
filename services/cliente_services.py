from container import back_produto, back_compra, back_item, back_cliente
from models.produto import Produto
from models.compra import Compra
from models.item import Item
import logging
from decimal import Decimal

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class ClienteServices():
    def __init__(self):
        pass

    def ver_produtos(self):
        try:
            produtos = back_produto.ver_produtos()

            if produtos:
                return produtos
            else:
                return []
        except Exception as e:
            logging.error(f'Falha ao buscar produtos no banco: {e}')
            return []
        
    def ver_produtos_preco_especificado(self, min, max):
        try:
            if isinstance(min, (Decimal, int, float)) and isinstance(max, (Decimal, int, float)):
                produtos = back_produto.ver_produtos()

                produtos_especificos = []

                if produtos:
                    for produto in produtos:
                        if produto.preco_unitario <= max and produto.preco_unitario >= min:
                            produtos_especificos.append(produto)
                    
                    return produtos_especificos
                else:
                    return []
            else:
                logging.error('Min e Max devem ser valores decimais ou inteiros')
                return []
        except Exception as e:
            logging.error(f'Falha ao visualizar produtos com preço especificado: {e}')
            return []

    def adicionar_produto_carrinho(self, id_usuario, id_produto, quantidade):
        try:
            clientes = back_cliente.ver_clientes()
            cliente_final = None

            if clientes:
                for cliente in clientes:
                    if cliente.usuario.id == id_usuario:
                        cliente_final = cliente
                        break

                if not cliente_final:
                    logging.error('Nenhum cliente final encontrado')
                    return False

            else:
                logging.error('Nenhum cliente encontrado')
                return False
            
            produtos = self.ver_produtos()
            produto_escolhido = None

            if produtos:
                for produto in produtos:
                    if produto.id == id_produto:
                        produto_escolhido = produto
                        break
                if not produto_escolhido:
                    return False
            else:
                logging.error('Nenhum produto encontrado')
                return False

            if quantidade <= produto_escolhido.estoque:
                preco_total = produto_escolhido.preco_unitario * quantidade
                carrinho = Compra(None, cliente_final, preco_total, None, None)
                verificar_cliente = False

                result_compra = None
                result_item = None
                compra_atual = None

                compra_status_aberto = back_compra.buscar_carrinho_aberto(cliente_final)

                if not compra_status_aberto:
                    result_compra = back_compra.adicionar_retornar(carrinho)
                    carrinho.id = result_compra[1]
                    compra_atual = carrinho
                else:
                    compra_status_aberto.preco_total = compra_status_aberto.preco_total + produto_escolhido.preco_unitario * quantidade
                    result_compra = back_compra.atualizar_retornar(compra_status_aberto)
                    compra_atual = compra_status_aberto

                if result_compra[0]:
                    item = Item(None, compra_atual, produto_escolhido, quantidade, produto_escolhido.preco_unitario)
                    result_item = back_item.adicionar(item)
                
                if result_compra[0] and result_item:
                    return True
                elif result_compra[0] and not result_item:
                    if not compra_status_aberto:
                        back_compra.remover(compra_atual)
                    return False
                else:
                    logging.error('Falha ao adicionar item e compra ao banco')
                    return False
        
        except Exception as e:
            logging.error(f'Erro ao adicionar produto ao carrinho: {e}')
            return False
        
    def atualizar_quantidade_produto_carrinho(self, item, quantidade):
        try:
            if quantidade <= item.produto.estoque:
                item.quantidade = quantidade

                result = back_item.atualizar(item)

                if result:
                    return True
                else:
                    return False
            else:
                return False
        except Exception as e:
            logging.error(f'Falha ao atualizar estoque do produto, {e}')

    def remover_produto_carrinho(self, item):
        try:
            result = back_item.remover(item)

            if result:
                return True
            else:
                return False
        except Exception as e:
            logging.error(f'Falha ao remover produto do banco de dados, {e}')
            return False