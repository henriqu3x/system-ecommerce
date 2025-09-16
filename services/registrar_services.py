import bcrypt
import logging
from models.usuario import Usuario
from models.admin import Admin
from models.cliente import Cliente
from main import back_usuario, back_admin, back_cliente

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class RegistrarServices():
    def __init__(self):
        pass

    def registrar(self, nome, email, senha, telefone, endereco):
        if nome and email and senha and telefone and endereco:
            senha_hash = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())

            if '@' in email:
                antes, depois = email.split('@', 1)
                if '.admin' in antes.lower():
                    perfil = 'admin'
                    usuario = Usuario(None, nome, email, senha_hash, perfil)
                    admin = Admin(None, usuario, nome, telefone, endereco)

                    result1 = back_usuario.adicionar(usuario)
                    if result1:
                        user = back_usuario.ver_usuario_especifico(usuario)

                        if user:
                            usuario.id = user.id
                        else:
                            return False
                        
                    result2 = back_admin.adicionar(admin)

                    if result1 and result2:
                        return True
                    elif result1 and not result2:
                        remocao_usu = back_usuario.remover(usuario)

                        if not remocao_usu:
                            logging.error('Não foi possivel remover o usuario, arquivo: registrar_services')
                            
                    elif not result1 and result2:
                        remocao_adm = back_admin.remover(admin)

                        if not remocao_adm:
                            logging.error('Não foi possivel remover o admin, arquivo: registrar_services')

                    return False
                else:
                    perfil = 'cliente'
                    usuario = Usuario(None, nome, email, senha_hash, perfil)
                    cliente = Cliente(None, usuario, nome, telefone, endereco)

                    result1 = back_usuario.adicionar(usuario)

                    if result1:
                        user = back_usuario.ver_usuario_especifico(usuario)

                        if user:
                            usuario.id = user.id
                        else:
                            return False
                        
                    result2 = back_cliente.adicionar(cliente)

                    if result1 and result2:
                        return True
                    elif result1 and not result2:
                        remocao_usu = back_usuario.remover(usuario)
                        if not remocao_usu:
                            logging.error('Não foi possivel remover o usuario, arquivo: registrar_service')
                    elif not result1 and result2:
                        remocao_cli = back_cliente.remover(cliente)
                        
                        if not remocao_cli:
                            logging.error('Não foi possivel remover o cliente, arquivo: registrar_services')

                    return False
                    
            else:
                return False
            
        else:
            return False