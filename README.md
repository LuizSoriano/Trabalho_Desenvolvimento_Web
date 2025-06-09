# Sistema de Venda de Ingressos - Documentação

## Visão Geral

Este é um sistema completo de venda de ingressos desenvolvido em Django, que permite gerenciar eventos, ingressos, clientes, compras e pagamentos. O sistema foi projetado seguindo o diagrama de classes fornecido, com Cliente herdando de User para autenticação.

## Estrutura do Projeto

```
Trabalho_Desenvolvimento_Web/
├── portal_vendas/                  # App Django principal
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── symple/                         # App de funcionalidades do sistema
│   ├── migrations/
│   ├── templates/
│   │   └──registration/
│   │       ├── login.html
│   │       └── register.html
│   │   └── symple/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── lista_eventos.html
│   │       └── detalhe_evento.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── static/                         # Pasta “origem” de arquivos estáticos
│   ├── img/
│   │   ├── fantasma_opera.jpg
│   │   ├── festival_rock.jpg
│   │   ├── final_campeonato.jpg
│   │   ├── placeholder_evento.jpg
│   │   └── pagamento/
│           ├── visa.svg
│           ├── mastercard.svg
│           ├── american_express.svg
│           └── pix.svg
├── criar_usuarios.py
├── manage.py
└── .gitignore                      # Arquivo de configuração do Git para ignorar arquivos e pastas

```

## Modelos de Dados

O sistema utiliza os seguintes modelos:

1. **Cliente**: Estende o modelo User do Django para autenticação
   - Campos: nome, email, cpf, telefone
   - Relacionamento: OneToOne com User

2. **Evento**: Representa eventos disponíveis
   - Campos: nome, data, local, capacidade, descrição, imagem
   - Métodos: ingressos_disponiveis()

3. **Ingresso**: Representa ingressos para eventos
   - Campos: preco, secao, evento (ForeignKey)

4. **Compra**: Representa compras realizadas pelos clientes
   - Campos: data_compra, cliente (ForeignKey), ingressos (ManyToMany)
   - Métodos: total()

5. **Pagamento**: Representa pagamentos associados às compras
   - Campos: metodo, status, compra (OneToOne), data_pagamento

## Funcionalidades Principais

### Para Visitantes
- Visualizar página inicial
- Visualizar lista de eventos
- Visualizar detalhes de eventos
- Registrar-se no sistema

### Para Clientes (Usuários Autenticados)
- Comprar ingressos
- Finalizar compras (checkout)
- Visualizar confirmação de compra
- Visualizar histórico de compras
- Gerenciar perfil de cliente

### Para Administradores
- Gerenciar eventos
- Gerenciar ingressos
- Gerenciar clientes
- Gerenciar compras
- Gerenciar pagamentos

## Instalação e Configuração

### Requisitos
- Python 3.8+
- Django 5.2+
- Pillow (para manipulação de imagens)

### Passos para Instalação

1. Clone o repositório:
```
git clone <url-do-repositorio>
```

2. Crie e ative um ambiente virtual:
```
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```
pip install django pillow
```

4. Execute as migrações:
```
python manage.py makemigrations
python manage.py migrate
```

5. Crie um superusuário:
```
python manage.py createsuperuser
```

6. Inicie o servidor de desenvolvimento:
```
python manage.py runserver
```

7. Acesse o sistema em: http://127.0.0.1:8000/

## Fluxo de Uso

### Registro e Login
1. Acesse a página inicial
2. Clique em "Entrar" no menu superior
3. Clique em "Cadastre-se" para criar uma nova conta
4. Preencha o formulário de registro e clique em "Cadastrar"
5. Complete seu perfil de cliente com nome, email, CPF e telefone

### Compra de Ingressos
1. Navegue pela lista de eventos ou busque eventos específicos
2. Clique em "Ver detalhes" para visualizar informações do evento
3. Escolha a seção desejada e clique em "Comprar"
4. Revise os detalhes da compra na página de checkout
5. Escolha o método de pagamento e preencha os dados necessários
6. Clique em "Finalizar Pagamento"
7. Visualize a confirmação da compra e os detalhes dos ingressos

### Administração
1. Acesse a área administrativa em: http://127.0.0.1:8000/admin/
2. Faça login com as credenciais de superusuário
3. Gerencie eventos, ingressos, clientes, compras e pagamentos

## Personalização

### Adicionando Novos Eventos
1. Acesse a área administrativa
2. Clique em "Eventos" > "Adicionar Evento"
3. Preencha os dados do evento e faça upload de uma imagem
4. Clique em "Salvar"

### Adicionando Ingressos para Eventos
1. Acesse a área administrativa
2. Clique em "Ingressos" > "Adicionar Ingresso"
3. Selecione o evento, defina a seção e o preço
4. Clique em "Salvar"

## Considerações para Produção

Antes de implantar em produção, considere:

1. Alterar a SECRET_KEY em settings.py
2. Definir DEBUG=False em settings.py
3. Configurar um banco de dados mais robusto (PostgreSQL, MySQL)
4. Configurar armazenamento de arquivos estáticos e de mídia
5. Configurar um servidor web como Nginx ou Apache
6. Configurar HTTPS para segurança

## Suporte e Manutenção

Para manutenção do sistema:

1. Atualize regularmente o Django e outras dependências
2. Faça backup regular do banco de dados
3. Monitore logs de erro para identificar problemas
4. Realize testes antes de implantar atualizações

## Conclusão

Este sistema de venda de ingressos oferece uma solução completa para gerenciar eventos, ingressos, clientes e pagamentos. Com uma interface amigável e funcionalidades robustas, o sistema atende às necessidades tanto de administradores quanto de clientes.