from django.contrib import admin
from .models import Cliente, Evento, Ingresso, Compra, Pagamento

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'telefone')
    search_fields = ('nome', 'email', 'cpf')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'local', 'capacidade', 'ingressos_disponiveis')
    search_fields = ('nome', 'local')
    list_filter = ('data',)

@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'secao', 'preco')
    list_filter = ('secao', 'evento')
    search_fields = ('evento__nome', 'secao')

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'data_compra', 'total')
    list_filter = ('data_compra',)
    search_fields = ('cliente__nome',)
    filter_horizontal = ('ingressos',)

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('compra', 'metodo', 'status', 'data_pagamento')
    list_filter = ('metodo', 'status', 'data_pagamento')
    search_fields = ('compra__cliente__nome',)
