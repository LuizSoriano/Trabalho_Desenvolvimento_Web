#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal_vendas.settings")
django.setup()

from django.contrib.auth.models import User
from symple.models import Cliente, Evento, Ingresso, Compra, Pagamento

print("Limpando dados antigos...")
Pagamento.objects.all().delete()
Compra.objects.all().delete()
Ingresso.objects.all().delete()
Evento.objects.all().delete()
Cliente.objects.all().delete()
User.objects.all().delete()
print("Dados antigos limpos.")

admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
print(f"Admin criado: {admin.username} / senha: admin123")

user1 = User.objects.create_user('maria', 'maria@example.com', 'maria123')
print(f"Usuário criado: {user1.username} / senha: maria123")

user2 = User.objects.create_user('joao', 'joao@example.com', 'joao123')
print(f"Usuário criado: {user2.username} / senha: joao123")

user3 = User.objects.create_user('ana', 'ana@example.com', 'ana123')
print(f"Usuário criado: {user3.username} / senha: ana123")

user4 = User.objects.create_user('carlos', 'carlos@example.com', 'carlos123')
print(f"Usuário criado: {user4.username} / senha: carlos123")

cliente1 = Cliente.objects.create(
    user=user1,
    nome="Maria Silva",
    email="maria@example.com",
    cpf="123.456.789-00",
    telefone="(11) 98765-4321"
)
print(f"Cliente criado: {cliente1.nome}")

cliente2 = Cliente.objects.create(
    user=user2,
    nome="João Santos",
    email="joao@example.com",
    cpf="987.654.321-00",
    telefone="(21) 91234-5678"
)
print(f"Cliente criado: {cliente2.nome}")

cliente3 = Cliente.objects.create(
    user=user3,
    nome="Ana Oliveira",
    email="ana@example.com",
    cpf="456.789.123-00",
    telefone="(51) 99876-5432"
)
print(f"Cliente criado: {cliente3.nome}")

cliente4 = Cliente.objects.create(
    user=user4,
    nome="Carlos Ferreira",
    email="carlos@example.com",
    cpf="789.123.456-00",
    telefone="(31) 98765-1234"
)
print(f"Cliente criado: {cliente4.nome}")

evento1 = Evento.objects.create(
    nome="Festival de Música Rock Brasil",
    data="2025-08-15",
    local="Estádio do Morumbi, São Paulo",
    capacidade=60000,
    descricao="O maior festival de rock do Brasil, com as principais bandas nacionais e internacionais."
)
print(f"Evento criado: {evento1.nome}")

evento2 = Evento.objects.create(
    nome="O Fantasma da Ópera",
    data="2025-07-20",
    local="Teatro Municipal, Rio de Janeiro",
    capacidade=2000,
    descricao="O clássico musical da Broadway chega ao Brasil em uma produção espetacular."
)
print(f"Evento criado: {evento2.nome}")

evento3 = Evento.objects.create(
    nome="Final do Campeonato Brasileiro",
    data="2025-12-10",
    local="Arena do Grêmio, Porto Alegre",
    capacidade=55000,
    descricao="A grande final do Campeonato Brasileiro de Futebol 2025."
)
print(f"Evento criado: {evento3.nome}")

ingresso1 = Ingresso.objects.create(preco=250.00, secao="VIP", evento=evento1)
ingresso2 = Ingresso.objects.create(preco=150.00, secao="Pista", evento=evento1)
ingresso3 = Ingresso.objects.create(preco=80.00, secao="Arquibancada", evento=evento1)

ingresso4 = Ingresso.objects.create(preco=180.00, secao="Plateia VIP", evento=evento2)
ingresso5 = Ingresso.objects.create(preco=120.00, secao="Plateia", evento=evento2)
ingresso6 = Ingresso.objects.create(preco=90.00, secao="Balcão", evento=evento2)

ingresso7 = Ingresso.objects.create(preco=300.00, secao="Camarote", evento=evento3)
ingresso8 = Ingresso.objects.create(preco=200.00, secao="Cadeiras Cobertas", evento=evento3)
ingresso9 = Ingresso.objects.create(preco=120.00, secao="Arquibancada", evento=evento3)

print(f"Criados {Ingresso.objects.count()} ingressos")

compra1 = Compra.objects.create(cliente=cliente1)
compra1.ingressos.add(ingresso1, ingresso2)
print(f"Compra criada para {compra1.cliente.nome}")

compra2 = Compra.objects.create(cliente=cliente2)
compra2.ingressos.add(ingresso4, ingresso5)
print(f"Compra criada para {compra2.cliente.nome}")

compra3 = Compra.objects.create(cliente=cliente3)
compra3.ingressos.add(ingresso7, ingresso8)
print(f"Compra criada para {compra3.cliente.nome}")

pagamento1 = Pagamento.objects.create(
    metodo="cartao_credito",
    status="aprovado",
    compra=compra1
)
print(f"Pagamento criado: {pagamento1.metodo} - {pagamento1.status}")

pagamento2 = Pagamento.objects.create(
    metodo="boleto",
    status="pendente",
    compra=compra2
)
print(f"Pagamento criado: {pagamento2.metodo} - {pagamento2.status}")

pagamento3 = Pagamento.objects.create(
    metodo="pix",
    status="aprovado",
    compra=compra3
)
print(f"Pagamento criado: {pagamento3.metodo} - {pagamento3.status}")

print("\nResumo dos dados criados:")
print(f"- {User.objects.count()} usuários")
print(f"- {Cliente.objects.count()} clientes")
print(f"- {Evento.objects.count()} eventos")
print(f"- {Ingresso.objects.count()} ingressos")
print(f"- {Compra.objects.count()} compras")
print(f"- {Pagamento.objects.count()} pagamentos")

print("\nCredenciais de acesso:")
print("Admin: admin / admin123")
print("Usuários: maria/maria123, joao/joao123, ana/ana123, carlos/carlos123")
