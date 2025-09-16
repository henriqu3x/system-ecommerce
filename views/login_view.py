from services.login_services import LoginServices
from views import app_view

def login(back_usuario):
    print('Login')

    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')

    login_services = LoginServices(back_usuario)
    result = login_services.login(email, senha)

    if result[0]:
        print('Usuario logado!')
        usuario_logado = result[1]
        print(f'Bem vindo {usuario_logado.nome}')
        app_view.main(usuario_logado)
        
    else:
        print('Email ou senha incorretos')

