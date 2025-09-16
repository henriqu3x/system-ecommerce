from models.usuario import Usuario
import bcrypt

class LoginServices():
    def __init__(self, dao):
        self.dao = dao

    def login(self, email, senha):
        if email and senha:
            usuario = Usuario(None, None, email, None, None)

            consultar_email = self.dao.ver_usuario_especifico(usuario)

            if consultar_email:
                senha_bytes = bytes(consultar_email.senha)
                if bcrypt.checkpw(senha.encode('utf-8'), senha_bytes):
                    return True, consultar_email
                else:
                    return False, None
            else:
                return False, None
        else:
            return False, None