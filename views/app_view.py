from views import login_view
from views import admin_view
from views import cliente_view

def main(usuario_logado):
    verificar_tipo = login_view.verificar_tipo(usuario_logado)

    if verificar_tipo == 'admin':
        admin_view.app_admin(usuario_logado)
    else:
        admin_view.app_admin(usuario_logado)