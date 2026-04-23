from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Usuario, Servico, Agendamento

def home(request):
    return render(request, 'home.html')

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('logado')  
        else:
            return render(request, 'login.html', {
                'erro': 'Usuário ou senha inválidos'
            })

    return render(request, 'login.html')

@login_required
def logado(request):
    return render(request, 'logado.html')

@login_required
def meus_agendamentos(request):
    meus_agendamentos = Agendamento.objects.all()
    return render(request, 'meus_agendamentos.html', {'meus_agendamentos': meus_agendamentos})

@login_required
def novo_agendamento(request):
    novo_agendamento = Agendamento.objects.all()
    return render(request, 'agendamento_form.html', {'novo_agendamento': novo_agendamento})

