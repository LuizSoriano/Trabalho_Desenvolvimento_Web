from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import logout
from .models import Evento, Ingresso, Compra, Pagamento, Cliente


def home(request):
    """
    View para a página inicial do sistema
    """
    eventos_destaque = Evento.objects.filter(data__gte=timezone.now()).order_by('data')[:6]
    return render(request, "symple/home.html", {
        'eventos_destaque': eventos_destaque
    })


def lista_eventos(request):
    """
    View para listar todos os eventos disponíveis
    """
    eventos = Evento.objects.filter(data__gte=timezone.now()).order_by('data')
    return render(request, "symple/lista_eventos.html", {
        'eventos': eventos
    })


def detalhe_evento(request, evento_id):
    """
    View para exibir detalhes de um evento específico
    """
    evento = get_object_or_404(Evento, pk=evento_id)
    ingressos = evento.ingressos.all()
    return render(request, "symple/detalhe_evento.html", {
        'evento': evento,
        'ingressos': ingressos
    })


@login_required
def comprar_ingresso(request, ingresso_id):
    """
    View para comprar um ingresso específico
    """
    ingresso = get_object_or_404(Ingresso, pk=ingresso_id)
    
    try:
        cliente = request.user.cliente
    except:
        messages.error(request, "Você precisa completar seu perfil de cliente antes de comprar ingressos.")
        return redirect('perfil_cliente')
    
    compra = Compra.objects.create(cliente=cliente)
    compra.ingressos.add(ingresso)
    
    return redirect('checkout', compra_id=compra.id)


@login_required
def checkout(request, compra_id):
    """
    View para finalizar uma compra
    """
    compra = get_object_or_404(Compra, pk=compra_id, cliente__user=request.user)
    
    if request.method == 'POST':
        metodo_pagamento = request.POST.get('metodo_pagamento')
        
        pagamento = Pagamento.objects.create(
            compra=compra,
            metodo=metodo_pagamento,
            status='aprovado' 
        )
        
        messages.success(request, "Compra realizada com sucesso!")
        return redirect('confirmacao_compra', pagamento_id=pagamento.id)
    
    return render(request, "symple/checkout.html", {
        'compra': compra
    })


@login_required
def confirmacao_compra(request, pagamento_id):
    """
    View para confirmar uma compra realizada
    """
    pagamento = get_object_or_404(Pagamento, pk=pagamento_id, compra__cliente__user=request.user)
    return render(request, "symple/confirmacao_compra.html", {
        'pagamento': pagamento
    })


@login_required
def minhas_compras(request):
    """
    View para listar as compras do usuário logado
    """
    try:
        cliente = request.user.cliente
        compras = cliente.compras.all().order_by('-data_compra')
    except:
        compras = []
    
    return render(request, "symple/minhas_compras.html", {
        'compras': compras
    })

def logout_confirm(request):
    """
    View para confirmar logout
    """
    return render(request, "symple/logout_confirm.html")

def custom_logout(request):
    """
    View personalizada para logout que funciona com GET e POST
    """
    logout(request)
    messages.success(request, "Você saiu do sistema com sucesso!")
    return redirect('home')


@login_required
def perfil_cliente(request):
    """
    View para exibir e editar o perfil do cliente
    """
    try:
        cliente = request.user.cliente
    except:
        cliente = None
    
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        
        if cliente:
            cliente.nome = nome
            cliente.email = email
            cliente.cpf = cpf
            cliente.telefone = telefone
            cliente.save()
        else:
            cliente = Cliente.objects.create(
                user=request.user,
                nome=nome,
                email=email,
                cpf=cpf,
                telefone=telefone
            )
        
        messages.success(request, "Perfil atualizado com sucesso!")
        return redirect('perfil_cliente')
    
    return render(request, "symple/perfil_cliente.html", {
        'cliente': cliente
    })
