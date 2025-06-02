from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    """
    View para registro de novos usuários
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Conta criada com sucesso! Complete seu perfil para continuar.")
            return redirect('perfil_cliente')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {
        'form': form
    })
