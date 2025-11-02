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
    insert into compra (cliente_id, preco_total_com) values
                                        (%s, %s)
                                        returning id_compra
''', (compra.cliente.id, compra.preco_total))
                
                
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

    def ver_compras(self, cliente:Cliente):
        try:
            dadosBrutos = self.consultar('''
    select id_compra, cliente_id, nome_cli, telefone_cli, preco_total_com, data_hora_com, status_com from compra
                                         inner join cliente on cliente_id = id_cliente where cliente_id = %s
''', (cliente.id, ))
            
            compras = []

            for dado in dadosBrutos:
                compra = Compra(dado[0], Cliente(dado[1], dado[2], dado[3], None, None), dado[4], dado[5], dado[6])
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
    update compra set cliente_id = %s, preco_total_com = %s, data_hora_com = %s, status_com = %s where id_compra = %s
''', (compra.cliente.id, compra.preco_total, compra.data_hora, compra.status, compra.id))
                
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

    def adicionar_retornar(self, compra:Compra):
        if compra:
            try:
                
                result = self.manipular_consultar('''
    insert into compra (cliente_id, preco_total_com) values
                                        (%s, %s)
                                        returning id_compra
''', (compra.cliente.id, compra.preco_total))
                
                
                if result[0]:
                    new_id = result[1]
                    return True, new_id
                else:
                    return False, None
            except Exception as e:
                logging.error(f'Falha ao tentar adicionar compra: {e}, arquivo: compraDAO')
                self.desconectar()
                return False, None
        else:
            logging.error('Nenhuma comprar inserida para ser adicionada, arquivo: compraDAO')
            return False, None
        
    def atualizar_retornar(self, compra:Compra):
        if compra:
            try:
                result = self.manipular_consultar('''
    update compra set cliente_id = %s, preco_total_com = %s, data_hora_com = %s, status_com = %s where id_compra = %s returning id_compra
''', (compra.cliente.id, compra.preco_total, compra.data_hora, compra.status, compra.id))
                
                if result[0]:
                    new_id = result[1]
                    return True, new_id
                else:
                    return False, None
            except Exception as e:
                logging.error(f'Falha ao atualizar compra: {e}, arquivo: compraDAO')
                self.desconectar()
                return False, None
        else:
            logging.error('Nenhuma compra inserida ao tentar atualizar, arquivo compraDAO')
            return False, None
        
    def buscar_carrinho_aberto(self, cliente:Cliente):
        try:
            dadosBrutos = self.consultar('''
    select id_compra, cliente_id, nome_cli, telefone_cli, preco_total_com, data_hora_com, status_com from compra
                                         inner join cliente on cliente_id = id_cliente
                                         where cliente_id = %s and status_com = 'aberto'
''', (cliente.id, ))

            for dado in dadosBrutos:
                compra = Compra(dado[0], Cliente(dado[1], dado[2], dado[3], None, None), dado[4], dado[5], dado[6])
                return compra

        except Exception as e:
            logging.error('Falha ao buscar carrinho aberto')
            return None