from db.connection import Connection
from models.admin import Admin
from models.usuario import Usuario
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class AdminDAO(Connection):
    def __init__(self, conexao):
        super().__init__(conexao.user, conexao.password, conexao.host, conexao.port, conexao.database)

    def adicionar(self, admin:Admin):
        if admin:
            try:
                result = self.manipular('''insert into admin (usuario_id, nome_adm, telefone_adm, endereco_adm) values
                                        (%s, %s, %s, %s)
                                        ''', (admin.usuario.id, admin.nome, admin.telefone, admin.endereco))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao adicionar admin: {e}, arquivo: adminDAO')
                self.desconectar()
                return False
        return False

    def ver_admins(self):
        try:
            dadosBrutos = self.consultar('''select id_admin, nome_adm, email_usu, telefone_adm, endereco_adm from admin
                                         inner join usuario on usuario_id = id_usuario
                                         ''')
            admins = []

            for dado in dadosBrutos:
                admin = Admin(dado[0], Usuario(None, None, dado[2], None, None), dado[1], dado[3], dado[4])
                admins.append(admin)

            return admins
        except Exception as e:
            logging.error(f'Não foi possivel visualizar os admins: {e}, arquivo: adminDAO')
            self.desconectar()
            return []

    def atualizar(self, admin:Admin):
        if admin:
            try:
                result = self.manipular('''
    update admin set usuario_id = %s, nome_adm = %s, telefone_adm = %s, endereco_adm = %s where id_admin = %s
''', (admin.usuario.id, admin.nome, admin.telefone, admin.endereco, admin.id))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Erro ao tentar atualizar admin: {e}, arquivo: adminDAO ')
                self.desconectar()
                return False
        else:
            logging.error('Nenhum admin inserido para atualização, arquivo: adminDAO')
            return False

    def remover(self, admin:Admin):
        if admin:
            try:
                result = self.manipular('delete from admin where id_admin = %s', (admin.id, ))

                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Não foi possivel deletar o admin: {e}, arquivo: adminDAO')
                self.desconectar()
                return False
        else:
            return False