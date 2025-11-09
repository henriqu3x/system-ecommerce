from container import back_compra, back_cliente, back_item
from models.compra import Compra
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class CompraServices():
    def __init__(self):
        pass

    def ver_carrinho(self, id_usuario):
        try:
            clientes = back_cliente.ver_clientes()
            cliente_final = None
            
            for cliente in clientes:
                if id_usuario == cliente.usuario.id:
                    cliente_final = cliente
                    break

            if cliente_final:
                compras = back_compra.ver_compras(cliente_final)
                compra_final = None

                if compras:
                    for compra in compras:
                        if compra.cliente.id == cliente_final.id and compra.status == 'aberto':
                            compra_final = compra
                            break
                else:
                    return []
                
                if compra_final:
                    itens = back_item.ver_itens(compra_final)

                    if itens:
                        return itens
                    else:
                        return []
                else:
                    return []
                
            else:
                return []


        except Exception as e:
            logging.error('Falha ao visualizar carrinho!')
            return [] 

    def finalizar_compra(self, id_usuario):
        try:
            carrinho = self.ver_carrinho(id_usuario)
            
            if not carrinho:
                return False
            
            compra_principal = carrinho[0].compra
                
            preco_total_att = sum(item.preco_unitario * item.quantidade for item in carrinho)

            compra_principal.preco_total = preco_total_att

            for item in carrinho:

                item.compra.status = 'pago'
                
                if item.produto.estoque < item.quantidade:
                    logging.warning(f'Estoque insuficiente para o produto ID: {item.produto.id}')
                    return False 
                    
                item.produto.estoque = item.produto.estoque - item.quantidade

                result = back_item.finalizar_compra_transacional(item)
                
                if not result:
                    logging.error(f'Falha ao atualizar item ID {item.id} durante a compra.')
                    return False 
                    
            return True 

        except Exception as e:
            logging.error(f'Falha catastrófica ao finalizar a compra para o usuário {id_usuario}, {e}')
            return False