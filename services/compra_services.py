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