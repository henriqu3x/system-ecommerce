from db.connection import Connection
import dotenv
import os
from controls.usuarioDAO import UsuarioDAO
from controls.adminDAO import AdminDAO
from controls.clienteDAO import ClienteDAO
from views import registrar_view, login_view

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

db = Connection(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

back_usuario = UsuarioDAO(db)
back_admin = AdminDAO(db)
back_cliente = ClienteDAO(db)

def main():

    while True:
        print('Sistema ecommerce')

        print('''
        1.Login
        2.Registrar
        0.Sair
    ''')
        
        op  = input('Selecione uma opção: ')

        if op == '1':
            login_view.login(back_usuario)
        elif op == '2':
            registrar_view.registrar()
        elif op == '0':
            print('SAINDO DO PROGRAMA...')
            break
        else:
            print('Opção invalida')

        input('APERTE QUALQUER BOTÃO PARA CONTINUAR')

if __name__ == '__main__':
    main()