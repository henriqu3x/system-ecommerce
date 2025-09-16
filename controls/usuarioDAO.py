from db.connection import Connection
from models.usuario import Usuario
import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class UsuarioDAO(Connection):
    def __init__(self, conexao):
        super().__init__(conexao.user, conexao.password, conexao.host, conexao.port, conexao.database)

    def adicionar(self, usuario:Usuario):
        if usuario:
            try:
                result = self.manipular('''insert into usuario (nome_usu, email_usu, senha_usu, perfil_usu) values
                                        (%s, %s, %s, %s)
                                        ''', (usuario.nome, usuario.email, usuario.senha, usuario.perfil))
                
                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Falha ao adicionar usuario: {e}, arquivo: usuarioDAO')
                self.desconectar()
                return False
        return False

    def ver_usuarios(self):
        try:
            dadosBrutos = self.consultar('select id_usuario, nome_usu, email_usu, perfil_usu from usuario')
            usuarios = []

            for dado in dadosBrutos:
                usuario = Usuario(dado[0], dado[1], dado[2], dado[3])
                usuarios.append(usuario)

            return usuarios
        except Exception as e:
            logging.error(f'Não foi possivel visualizar os usuarios: {e}, arquivo: usuarioDAO')
            self.desconectar()
            return []
        
    def ver_usuario_especifico(self, usuario:Usuario):
        try:
            dadosBrutos = self.consultar('select id_usuario, nome_usu, email_usu, senha_usu, perfil_usu from usuario where email_usu = %s', (usuario.email, ))
            user = None

            for dado in dadosBrutos:
                u = Usuario(dado[0], dado[1], dado[2], dado[3], dado[4])
                user = u
                break

            return user
        except Exception as e:
            logging.error(f'Não foi possivel visualizar o usuario: {e}, arquivo: usuarioDAO')
            self.desconectar()
            return []

    def atualizar(self):
        pass

    def remover(self, usuario:Usuario):
        if usuario:
            try:
                result = self.manipular('delete from usuario where id_usuario = %s', (usuario.id, ))

                if result:
                    return True
                else:
                    return False
            except Exception as e:
                logging.error(f'Não foi possivel deletar o usuario: {e}, arquivo: usuarioDAO')
                self.desconectar()
                return False
        else:
            return False
