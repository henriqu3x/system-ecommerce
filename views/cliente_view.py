from services.cliente_services import ClienteServices
cliente_services = ClienteServices()
from models.usuario import Usuario
from decimal import Decimal

def ver_produtos():
    produtos = cliente_services.ver_produtos()

    if produtos:
        for produto in produtos:
            print(f'ID: {produto.id} | NOME: {produto.nome} | CATEGORIA: {produto.categoria} | ESTOQUE: {produto.estoque} | PREÇO: {produto.preco_unitario}')
    else:
        print('Nenhum produto cadastrado no momento, Tente novamente mais tarde')

    return produtos

def ver_produtos_preco_especificado():
    try:
        pMin = Decimal(input('Digite o preço minimo: '))
        pMax = Decimal(input('Digite o preço maximo: '))
        produtos = cliente_services.ver_produtos_preco_especificado(pMin, pMax)

        if produtos:
            for produto in produtos:
                print(f'ID: {produto.id} | NOME: {produto.nome} | CATEGORIA: {produto.categoria} | ESTOQUE: {produto.estoque} | PREÇO: {produto.preco_unitario}')

        else:
            print('Nenhum produto encontrado com as especificações desejadas')

        return produtos
    except Exception as e:
        print('Falha ao enviar preços, digite somente numeros')

def adicionar_produto_carrinho(usuario:Usuario):
    try:
        id_usuario = int(usuario.id)
        produtos = ver_produtos()
        if produtos:
            id_produto = int(input('Digite o id do produto escolhido: '))
            quantidade = int(input('Digite a quantidade que será adicionada ao carrinho: '))

            for produto in produtos:
                if produto.id == id_produto:
                    if produto.estoque >= quantidade:
                        result = cliente_services.adicionar_produto_carrinho(id_usuario, id_produto, quantidade)

                        if result:
                            print('Produto adicionado ao carrinho!')
                        else:
                            print('Falha ao adicionar produto ao carrinho')
                        break
                    else:
                        print('O produto escolhido não tem estoque suficiente para a quantidade desejada')
                else:
                    print('Insira um id valido')        
        else:
            print('Nenhum produto encontrado!')
    except Exception as e:
        print(f'Falha ao enviar produto para ser adicionado ao carrinho: {e}')

def atualizar_quantidade_produto_carrinho():
    pass

def remover_produto_carrinho():
    pass

def finalizar_compra():
    pass

def app_cliente(usuario):
    while True:
        print('Menu Cliente')

        print('''
    1. Ver Produtos
    2. Ver Produtos com preço especificado
    3. Adicionar Produtos ao carrinho
    4. Atualizar a quantidade de um produto do carrinho
    5. Remover produtos do carrinho
    6. Finalizar Compra
    0. Voltar
''')
        
        op = input('Selecione uma opção: ')

        if op == '0':
            print('Voltando...')
            break
        elif op == '1':
            ver_produtos()
        elif op == '2':
            ver_produtos_preco_especificado()
        elif op == '3':
            adicionar_produto_carrinho(usuario)
        elif op == '4':
            atualizar_quantidade_produto_carrinho()
        elif op == '5':
            remover_produto_carrinho()
        elif op == '6':
            finalizar_compra()
        else:
            print('Selecione uma opção valida')

        input('APERTE QUALQUER BOTÃO PARA CONTINUAR...')