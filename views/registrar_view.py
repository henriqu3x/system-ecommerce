from services.registrar_services import RegistrarServices

def registrar():
    print('Registrar')

    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    senha = input('Digite sua senha: ')
    telefone = input('Digite seu telefone: ')
    endereco = input('Digite seu endereço: ')

    services_registrar = RegistrarServices()

    result = services_registrar.registrar(nome, email, senha, telefone, endereco)

    if result:
        print('Usuario registrado com sucesso!')
    else:
        print('Falha ao registrar usuario')


