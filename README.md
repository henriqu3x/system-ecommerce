# Sistema E-commerce

Um sistema de e-commerce para portfolio desenvolvido em Python que permite aos usuários se registrarem como clientes ou administradores, gerenciar produtos e realizar compras através de uma interface de linha de comando.

## 📋 Funcionalidades

### Para Clientes:
- **Registro e Login**: Criação de conta e autenticação
- **Visualização de Produtos**: Listar todos os produtos disponíveis
- **Busca por Preço**: Filtrar produtos por faixa de preço
- **Carrinho de Compras**: Adicionar, atualizar quantidade e remover itens
- **Finalização de Compras**: Concluir pedidos

### Para Administradores:
- **Gerenciamento de Produtos**: CRUD completo (Criar, Ler, Atualizar, Deletar)
- **Controle de Estoque**: Atualização de quantidades em estoque
- **Relatórios**: Visualização de produtos com baixo estoque (≤15 unidades)
- **Atualização de Preços**: Modificação de preços de produtos

## 🏗️ Arquitetura

O projeto segue o padrão arquitetural **MVC (Model-View-Controller)** com camadas adicionais:

```
system-ecommerce/
├── main.py                 # Ponto de entrada da aplicação
├── container.py            # Configuração de dependências e injeção
├── db/                     # Camada de acesso a dados
│   ├── connection.py       # Conexão com PostgreSQL
│   └── setup.py           # Scripts de criação das tabelas
├── models/                 # Camada de modelos (entidades)
│   ├── usuario.py
│   ├── cliente.py
│   ├── admin.py
│   ├── produto.py
│   ├── compra.py
│   └── item.py
├── controls/               # Data Access Objects (DAOs)
│   ├── usuarioDAO.py
│   ├── clienteDAO.py
│   ├── adminDAO.py
│   ├── produtoDAO.py
│   ├── compraDAO.py
│   └── itemDAO.py
├── services/               # Camada de lógica de negócio
│   ├── login_services.py
│   ├── registrar_services.py
│   ├── admin_services.py
│   ├── cliente_services.py
│   └── compra_services.py
└── views/                  # Camada de apresentação (interface)
    ├── login_view.py
    ├── registrar_view.py
    ├── admin_view.py
    ├── cliente_view.py
    └── app_view.py
```

## 🗄️ Banco de Dados

### Tecnologias:
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional
- **psycopg2**: Driver Python para PostgreSQL

## 🚀 Instalação e Configuração

### Pré-requisitos:
- Python 3.8+
- PostgreSQL
- pip (gerenciador de pacotes Python)

### Passos:

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd system-ecommerce
   ```

2. **Instale as dependências:**
   ```bash
   pip install psycopg2-binary python-dotenv
   ```

3. **Configure o banco de dados:**
   - Crie um banco de dados PostgreSQL
   - Crie um arquivo `.env` na raiz do projeto:
     ```
     DB_NAME=nome_do_banco
     DB_USER=seu_usuario
     DB_PASSWORD=sua_senha
     DB_HOST=localhost
     DB_PORT=5432
     ```

4. **Execute o setup do banco:**
   ```bash
   python db/setup.py
   ```

5. **Execute a aplicação:**
   ```bash
   python main.py
   ```

## 📖 Como Usar

### Fluxo Básico:

1. **Registro**: Escolha a opção 2 no menu principal para criar uma conta
2. **Login**: Use a opção 1 para fazer login
3. **Menu Principal**:
   - **Clientes**: Visualizar produtos, gerenciar carrinho, finalizar compras
   - **Administradores**: Gerenciar catálogo de produtos

### Menus Disponíveis:

#### Menu Principal:
- 1. Login
- 2. Registrar
- 0. Sair

#### Menu Cliente:
- 1. Ver Produtos
- 2. Ver Produtos com preço especificado
- 3. Ver Carrinho
- 4. Adicionar Produtos ao carrinho
- 5. Atualizar quantidade de produto no carrinho
- 6. Remover produtos do carrinho
- 7. Finalizar Compra
- 0. Voltar

#### Menu Administrador:
- 1. Cadastrar Produto
- 2. Ver Produtos
- 3. Ver produtos com estoque ≤15
- 4. Atualizar Estoque de produto
- 5. Atualizar Preços de um produto
- 6. Atualizar Produto
- 7. Deletar Produto
- 0. Voltar

## 🔧 Tecnologias Utilizadas

- **Linguagem**: Python 3.8+
- **Banco de Dados**: PostgreSQL
- **Driver DB**: psycopg2
- **Gerenciamento de Configurações**: python-dotenv
- **Padrão Arquitetural**: MVC com Services Layer

## 📝 Características Técnicas

- **Tratamento de Erros**: Logging abrangente para debugging
- **Validações**: Constraints no banco e validações na aplicação
- **Segurança**: Senhas armazenadas como hash
- **Transações**: Controle de estoque e integridade de dados
- **Separação de Responsabilidades**: Camadas bem definidas

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- **Desenvolvedor**: Luiz Henrique
- **Curso**: Tecnico em Desenvolvimento de Sistemas - UC 6

---

**Nota**: Este é um projeto acadêmico desenvolvido para fins de aprendizado e demonstração de conceitos de desenvolvimento de software.
