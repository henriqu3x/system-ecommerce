from views import login_view, registrar_view
from container import back_usuario

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