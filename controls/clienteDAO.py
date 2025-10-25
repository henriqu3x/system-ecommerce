from db.connection import Connection
from models.cliente import Cliente
from models.usuario import Usuario
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class ClienteDAO(Connection):
    def __init__(self, conexao):
        super().__init__(conexao.user, conexao.password, conexao.host, conexao.port, conexao.database)

    def adicionar(self, cliente:Cliente):
        if cliente:
            try:
                result = self.manipular('''insert into cliente (usuario_id, nome_cli, telefone_cli, endereco_cli) values
                                        (%s, %s, %s, %s)
                                        ''', (cliente.usuario.id, cliente.nome, cliente.telefone, cliente.endereco))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao adicionar cliente: {e}, arquivo: clienteDAO')
                self.desconectar()
                return False
        return False

    def ver_clientes(self):
        try:
            dadosBrutos = self.consultar('''select id_cliente, usuario_id, nome_cli, email_usu, telefone_cli, endereco_cli from cliente
                                         inner join usuario on usuario_id = id_usuario
                                         ''')
            clientes = []

            for dado in dadosBrutos:
                cliente = Cliente(dado[0], Usuario(dado[1], dado[2], dado[3], None, None), dado[2], dado[4], dado[5])
                clientes.append(cliente)

            return clientes
        except Exception as e:
            logging.error(f'Não foi possivel visualizar os clientes: {e}, arquivo: clienteDAO')
            self.desconectar()
            return []

    def atualizar(self, cliente:Cliente):
        if cliente:
            try:
                result = self.manipular('''
    update cliente set usuario_id = %s, nome_cli = %s, telefone_cli = %s, endereco_cli = %s where id_cliente = %s
                                        
    ''', (cliente.usuario.id, cliente.nome, cliente.telefone, cliente.endereco, cliente.id))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Erro ao tentar atualizar cliente: {e}, arquivo: clienteDAO')
                self.desconectar()
                return False
        else:
            logging.error('Nenhum cliente inserido para ser atualizado, arquivo: clienteDAO')
            return False

    def remover(self, cliente:Cliente):
        if cliente:
            try:
                result = self.manipular('delete from cliente where id_cliente = %s', (cliente.id, ))

                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Não foi possivel deletar o cliente: {e}, arquivo: clienteDAO')
                self.desconectar()
                return False
        else:
            return False