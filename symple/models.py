from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Cliente(models.Model):
    """
    Modelo de Cliente que herda de User para autenticação
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    """
    Modelo para Eventos disponíveis no sistema
    """
    nome = models.CharField(max_length=255)
    data = models.DateField()
    local = models.CharField(max_length=255)
    capacidade = models.PositiveIntegerField()
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='eventos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nome} - {self.data}"
    
    def ingressos_disponiveis(self):
        """Retorna a quantidade de ingressos disponíveis"""
        vendidos = sum(ingresso.compras.count() for ingresso in self.ingressos.all())
        return self.capacidade - vendidos


class Ingresso(models.Model):
    """
    Modelo para Ingressos de eventos
    """
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    secao = models.CharField(max_length=100)
    evento = models.ForeignKey(Evento, related_name='ingressos', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.evento.nome} - {self.secao} - R${self.preco}"


class Compra(models.Model):
    """
    Modelo para Compras realizadas pelos clientes
    """
    data_compra = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(Cliente, related_name='compras', on_delete=models.CASCADE)
    ingressos = models.ManyToManyField(Ingresso, related_name='compras')
    
    def __str__(self):
        return f"Compra {self.id} - {self.cliente.nome}"
    
    def total(self):
        """Calcula o valor total da compra"""
        return sum(ingresso.preco for ingresso in self.ingressos.all())


class Pagamento(models.Model):
    """
    Modelo para Pagamentos associados às compras
    """
    METODO_CHOICES = [
        ('cartao_credito', 'Cartão de Crédito'),
        ('cartao_debito', 'Cartão de Débito'),
        ('pix', 'PIX'),
        ('boleto', 'Boleto Bancário'),
    ]
    
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
        ('cancelado', 'Cancelado'),
    ]
    
    metodo = models.CharField(max_length=50, choices=METODO_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pendente')
    compra = models.OneToOneField(Compra, related_name='pagamento', on_delete=models.CASCADE)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Pagamento {self.id} - {self.get_metodo_display()} - {self.get_status_display()}"
