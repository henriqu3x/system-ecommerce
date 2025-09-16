import logging
from models.compra import Compra
from models.cliente import Cliente
from db.connection import Connection

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class CompraDAO(Connection):
    def __init__(self, conexao):
        super().__init__(conexao.user, conexao.password, conexao.host, conexao.port, conexao.database)

    def adicionar(self, compra:Compra):
        if compra:
            try:
                result = self.manipular('''
    insert into compra (cliente_id, preco_total_com, data_hora_com) values
                                        (%s, %s, %s)
''', (compra.cliente.id, compra.preco_total, compra.data_hora))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao tentar adicionar compra: {e}, arquivo: compraDAO')
                self.desconectar()
                return False
        else:
            logging.error('Nenhuma comprar inserida para ser adicionada, arquivo: compraDAO')
            return False

    def ver_compras(self):
        try:
            dadosBrutos = self.consultar('''
    select id_compra, cliente_id, nome_cli, telefone_cli, preco_total_com, data_hora_com from compra
                                         inner join cliente on cliente_id = id_cliente
''')
            
            compras = []

            for dado in dadosBrutos:
                compra = Compra(dado[0], Cliente(dado[1], dado[2], dado[3], None), dado[4], dado[5])
                compras.append(compra)
            
            return compras
        except Exception as e:
            logging.error(f'Falha ao visualizar compras {e}, arquivo: compraDAO')
            self.desconectar()
            return []

    def atualizar(self, compra:Compra):
        if compra:
            try:
                result = self.manipular('''
    update compra set cliente_id = %s, preco_total_com = %s, data_hora_com = %s where id_compra = %s
''', (compra.cliente.id, compra.preco_total, compra.data_hora, compra.id))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao atualizar compra: {e}, arquivo: compraDAO')
                self.desconectar()
                return False
        else:
            logging.error('Nenhuma compra inserida ao tentar atualizar, arquivo compraDAO')
            return False

    def remover(self, compra:Compra):
        if compra:
            try:
                result = self.manipular('delete from compra where id_compra = %s', (compra.id, ))

                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao tentar remover compra: {e}, arquivo: compraDAO')
                self.desconectar()
                return False
        else:
            logging.error('Nenhuma compra inserida para a tentativa de remoção, arquivo: compraDAO')
            return False
