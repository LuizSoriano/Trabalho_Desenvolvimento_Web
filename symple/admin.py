from django.contrib import admin
from .models import Evento, Ingresso, Cliente, Compra, Pagamento

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ("nome", "data", "local", "capacidade")

@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    list_display = ("evento", "secao", "preco")

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "cpf", "telefone")

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "data_compra")
    filter_horizontal = ("ingressos",)

@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ("compra", "metodo", "status")
