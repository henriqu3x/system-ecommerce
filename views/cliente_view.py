from services.cliente_services import ClienteServices
cliente_services = ClienteServices()
from services.compra_services import CompraServices
compra_services = CompraServices()
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

def ver_carrinho(usuario):
    try:
        id_usuario = int(usuario.id)
        ver_carrinho = compra_services.ver_carrinho(id_usuario)

        if ver_carrinho:
            for item in ver_carrinho:
                print(f"""
        ID do Item: {item.id}
        ID da Compra: {item.compra.id}
        Produto: {item.produto.nome}
        Categoria: {item.produto.categoria}
        Estoque: {item.produto.estoque}
        Quantidade: {item.quantidade}
        Preço Unitário (Item): {item.preco_unitario}
        """)
        
            return ver_carrinho
        else:
            print('Nenhum item no carrinho!')
            return []
                
        
    except Exception as e:
        print(f'Falha ao ver carrinho, {e}')

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
            print('Nenhum produto encontrado!')
    except Exception as e:
        print(f'Falha ao enviar produto para ser adicionado ao carrinho: {e}')

def atualizar_quantidade_produto_carrinho(usuario):
    try:
        carrinho = ver_carrinho(usuario)

        if carrinho:  
            id_item = int(input('Digite o id do item que voce deseja alterar a quantidade: '))
            item_selecionado = None

            for item in carrinho:
                if item.id == id_item:
                    item_selecionado = item
                    break
            
            if not item_selecionado:
                print('Nenhum item encontrado para o id selecionado')
                return

            quantidade = int(input('Qual a nova quantidade: '))

            result = cliente_services.atualizar_quantidade_produto_carrinho(item_selecionado, quantidade)

            if result:
                print('Quantidade do produto atualizada com sucesso!')
            else:
                print('Falha ao atualizar quantidade do produto no carrinho')
        else:
            print('Nenhuma compra encontrada')
        
    except Exception as e:
        print(f'Falha ao atualizar quantidade, {e}')
    except ValueError as e:
        print('Insira numeros validos para o id e quantidade')

def remover_produto_carrinho(usuario):
    try:
        carrinho = ver_carrinho(usuario)
        if carrinho:
            id_item = int(input('Digite o id do item que voce deseja remover: '))
            item_selecionado = None

            for item in carrinho:
                if item.id == id_item:
                    item_selecionado = item
                    break

            if not item_selecionado:
                print('Nenhum item encontrado para o id selecionado')
                return
            
            result = cliente_services.remover_produto_carrinho(item)

            if result:
                print('Sucesso ao remover produto do carrinho')
            else:
                print('Falha ao remover produto do carrinho')
        else:
            print('Nenhuma compra encontrada')
                
    except Exception as e:
        print(f'Falha ao remover produto, {e}')
    except ValueError as e:
        print(f'Insira um numero valido para o id')

def finalizar_compra(usuario):
    try:
        carrinho = ver_carrinho(usuario)
        preco_total = 0

        for item in carrinho:
            preco_total = sum(item.preco_unitario * item.quantidade for item in carrinho)

        result = compra_services.finalizar_compra(usuario.id)

        if result:
            print(f'Compra finalizada com sucesso!, Total pago: {preco_total}')
        else:
            print('Falha ao finalizar compra, verifique se voce tem itens no carrinho ou se o produto tem estoque disponivel')

    except Exception as e:
        print(f'Ocorreu um erro ao finalizar a compra, {e}')

def app_cliente(usuario):
    while True:
        print('Menu Cliente')

        print('''
    1. Ver Produtos
    2. Ver Produtos com preço especificado
    3. Ver Carrinho
    4. Adicionar Produtos ao carrinho
    5. Atualizar a quantidade de um produto do carrinho
    6. Remover produtos do carrinho
    7. Finalizar Compra
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
            ver_carrinho(usuario)
        elif op == '4':
            adicionar_produto_carrinho(usuario)
        elif op == '5':
            atualizar_quantidade_produto_carrinho(usuario)
        elif op == '6':
            remover_produto_carrinho(usuario)
        elif op == '7':
            finalizar_compra(usuario)
        else:
            print('Selecione uma opção valida')

        input('APERTE QUALQUER BOTÃO PARA CONTINUAR...')