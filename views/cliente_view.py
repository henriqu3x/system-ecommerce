from services.cliente_services import ClienteServices
cliente_services = ClienteServices()
from decimal import Decimal

def ver_produtos():
    produtos = cliente_services.ver_produtos()

    if produtos:
        for produto in produtos:
            print(f'ID: {produto.id} | NOME: {produto.nome} | CATEGORIA: {produto.categoria} | ESTOQUE: {produto.estoque} | PREÇO: {produto.preco_unitario}')
    else:
        print('Nenhum produto cadastrado no momento, Tente novamente mais tarde')

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
    except Exception as e:
        print('Falha ao enviar preços, digite somente numeros')

def adicionar_produto_carrinho():
    pass

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
            adicionar_produto_carrinho()
        elif op == '4':
            atualizar_quantidade_produto_carrinho()
        elif op == '5':
            remover_produto_carrinho()
        elif op == '6':
            finalizar_compra()
        else:
            print('Selecione uma opção valida')

        input('APERTE QUALQUER BOTÃO PARA CONTINUAR...')