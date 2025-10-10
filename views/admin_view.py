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

def ver_produtos():
    produtos = admin_services.ver_produtos()

    if produtos:
        for produto in produtos:
            print(f'ID: {produto.id} | NOME: {produto.nome} | CATEGORIA: {produto.categoria} | ESTOQUE: {produto.estoque} | PREÇO: {produto.preco_unitario}')
    else:
        print('Sem produtos cadastrados no momento')

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
    ver_produtos()
    try:
        id_produto = int(input('Digite o id do produto escolhido: '))
        preco = float(input('Digite o novo preço do produto: '))

        result = admin_services.atualizar_preco_produto(id_produto, preco)

        if result:
            print('Preço do produto atualizado com sucesso!')
        else: 
            print('Falha ao atualizar o preço do produto')
    except Exception as e:
        print('Falha ao converter o id ou o preço')

def atualizar_produto():
    ver_produtos()
    try:
        id_produto = int(input('Digite o id do produto selecionado: '))
        nome_produto = input('Digite o nome do produto (ou deixe em branco para continuar como esta): ')
        categoria_produto = input('Digite a categoria do produto (ou deixe em branco para continuar como esta): ')
        estoque_produto = input('Digite o estoque do produto (ou deixe em branco para continuar como esta): ')
        preco_produto = input('Digite o preço do produto (ou deixe em branco para continuar como esta): ')

        result = admin_services.atualizar_produto(id_produto, nome_produto, categoria_produto, estoque_produto, preco_produto)

        if result: 
            print('Produto atualizado com sucesso!')
        else:
            print('Falha ao atualizar produto')
    except Exception as e:
        print(f'Falha ao enviar dados do produto para atualização {e}')

def remover_produto():
    ver_produtos()
    try:
        id_produto = int(input('Digite o id do produto que será removido: '))
        confirm = input('Voce tem certeza que deseja remover esse produto? (s/n): ').lower()

        if confirm in ['s', 'sim']:
            result = admin_services.remover_produto(id_produto)

            if result:
                print('Produto deletado com sucesso!')
            else:
                print('Falha ao deletar produto')
        else:
            print('Remoção de produto cancelada')
    except Exception as e:
        print(f'Falha ao enviar produto para ser removido {e}')


def app_admin(usuario):
    while True:
        print('Menu Admin')

        print('''
    1.Cadastrar Produto
    2.Ver Produtos
    3.Ver produtos com estoque 15 ou menor
    4.Atualizar Estoque de produto
    5.Atualizar Preços de um produto
    6.Atualizar Produto
    7.Deletar Produto
    0.Voltar
''')
        
        op = input('SELECIONE UMA OPÇÃO: ')

        if op == '1':
            cadastrar_produto()
        elif op == '2':
            ver_produtos()
        elif op == '3':
            ver_produtos_estoque15()
        elif op == '4':
            atualizar_estoque_produto()
        elif op == '5':
            atualizar_preco_produto()
        elif op == '6':
            atualizar_produto()
        elif op == '7':
            remover_produto()
        elif op == '0':
            print('VOLTANDO...')
            break
        else:
            print('Opção invalida!')

        input('APERTE QUALQUER BOTÃO PARA CONTINUAR')
