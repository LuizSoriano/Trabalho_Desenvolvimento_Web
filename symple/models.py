from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    local = models.CharField(max_length=255)
    capacidade = models.PositiveIntegerField()

class Ingresso(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    secao = models.CharField(max_length=100)
    evento = models.ForeignKey(Evento, related_name='ingressos', on_delete=models.CASCADE)

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)

class Compra(models.Model):
    data_compra = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, related_name='compras', on_delete=models.CASCADE)
    ingressos = models.ManyToManyField(Ingresso, related_name='compras')

class Pagamento(models.Model):
    metodo = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    compra = models.OneToOneField(Compra, related_name='pagamento', on_delete=models.CASCADE)
