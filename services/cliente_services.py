from container import back_produto
from models import produto
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

