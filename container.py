from db.connection import Connection
import dotenv
import os
from controls.usuarioDAO import UsuarioDAO
from controls.adminDAO import AdminDAO
from controls.clienteDAO import ClienteDAO
from controls.produtoDAO import ProdutoDAO

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
back_produto = ProdutoDAO(db)

