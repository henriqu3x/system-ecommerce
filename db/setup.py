from connection import Connection
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

db = Connection(DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)

db.manipular('drop table if exists item')
db.manipular('drop table if exists compra')
db.manipular('drop table if exists cliente')
db.manipular('drop table if exists admin')
db.manipular('drop table if exists usuario')
db.manipular('drop table if exists produto')

db.manipular('''create table if not exists produto(
             id_produto int generated always as identity primary key,
             nome_pro varchar(50) not null default 'produto sem nome',
             categoria_pro varchar(50) not null default 'produto sem categoria',
             estoque_pro int not null,
             preco_unitario_pro decimal(8,2) not null,
             constraint chk_estoque check(estoque_pro >= 0),
             constraint chk_preco check(preco_unitario_pro > 0)
             )''')

db.manipular('''
    create table if not exists usuario(
             id_usuario int generated always as identity primary key,
             nome_usu varchar(50) not null default 'sem nome de usuario',
             email_usu varchar(50) not null unique,
             senha_usu bytea not null,
             perfil_usu varchar(20) not null,
             constraint chk_email check(email_usu like '_%@_%'),
             constraint chk_perfil check(perfil_usu in ('cliente', 'admin'))
             )
''')

db.manipular('''
    create table if not exists cliente(
             id_cliente int generated always as identity primary key,
             usuario_id int not null,
             nome_cli varchar(50) not null default 'sem nome de cliente',
             telefone_cli varchar(25) not null,
             endereco_cli varchar(50) not null,
             constraint fk_cliente_usuario foreign key (usuario_id) references usuario(id_usuario)
             )
''')

db.manipular('''
    create table if not exists compra(
             id_compra int generated always as identity primary key,
             cliente_id int not null,
             preco_total_com decimal(8,2) not null,
             data_hora_com timestamp default current_timestamp,
             status_com varchar(50) default 'aberto',
             constraint chk_status check(status_com in ('aberto','fechado','pago')),
             constraint chk_preco_total check(preco_total_com > 0),
             constraint fk_compra_cliente foreign key (cliente_id) references cliente(id_cliente)
             )
''')

db.manipular('''
create table if not exists admin(
             id_admin int generated always as identity primary key,
             usuario_id int not null,
             nome_adm varchar(50) not null,
             telefone_adm varchar(25) not null,
             endereco_adm varchar(50) not null,
             constraint fk_admin_usuario foreign key (usuario_id) references usuario(id_usuario)
             )
''')


db.manipular('''
    create table if not exists item(
             id_item int generated always as identity primary key,
             compra_id int not null,
             produto_id int not null,
             quantidade_ite int not null,
             preco_unitario_ite decimal(8,2) not null,
             constraint chk_quantidade check(quantidade_ite > 0),
             constraint chk_preco_unitario check(preco_unitario_ite > 0),
             constraint fk_item_compra foreign key (compra_id) references compra(id_compra),
             constraint fk_item_produto foreign key (produto_id) references produto(id_produto)
             )
''')