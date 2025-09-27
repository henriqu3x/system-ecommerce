from services.admin_services import AdminServices
admin_services = AdminServices()

def cadastrar_produto():
    nome = input('Digite o nome do produto: ')
    categoria = input('Digite a categoria do produto: ')
    estoque = int(input('Digite o estoque do produto: '))
    preco = input('Digite o preço do produto: ')

    result = admin_services.cadastrar_produto(nome, categoria, estoque, preco)

    if result:
        print('Produto cadastrado com sucesso!')
    else:
        print('Falha ao cadastrar produto')

def ver_produtos_estoque15():
    produtos = admin_services.ver_produtos_estoque15()

    if produtos:
        for produto in produtos:
            print(f'ID: {produto.id} | NOME: {produto.nome} | CATEGORIA: {produto.categoria} | ESTOQUE: {produto.estoque} | PREÇO: {produto.preco_unitario}')
    else:
        print('Sem produtos com estoque em 15 ou abaixo')

def atualizar_estoque_produto():
    ver_produtos_estoque15()
    try:
        id_produto = int(input('Digite o id do produto escolhido: '))
        qtd_estoque = int(input('Insira o novo estoque do produto: '))
        
        result = admin_services.atualizar_estoque_produto(id_produto, qtd_estoque)
        if result:
            print('Estoque do produto atualizado com sucesso!')
        else:
            print('Falha ao atualizar estoque do produto')
    except ValueError as e:
        print('Id ou estoque invalidos')
        
    

def atualizar_preco_produto():
    pass

def atualizar_produto():
    pass

def remover_produto():
    pass


def app_admin(usuario):
    while True:
        print('Menu Admin')

        print('''
    1.Cadastrar Produto
    2.Ver produtos com estoque 15 ou menor
    3.Atualizar Estoque de produto
    4.Atualizar Preços de um produto
    5.Atualizar Produto
    6.Deletar Produto
    0.Voltar
''')
        
        op = input('SELECIONE UMA OPÇÃO: ')

        if op == '1':
            cadastrar_produto()
        elif op == '2':
            ver_produtos_estoque15()
        elif op == '3':
            atualizar_estoque_produto()
        elif op == '4':
            atualizar_preco_produto()
        elif op == '5':
            atualizar_produto()
        elif op == '6':
            remover_produto()
        elif op == '0':
            print('VOLTANDO...')
            break
        else:
            print('Opção invalida!')

        input('APERTE QUALQUER BOTÃO PARA CONTINUAR')
