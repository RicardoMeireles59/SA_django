from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Usuario, Servico, Agendamento
from datetime import datetime
from django.contrib import messages
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AgendamentoSerializer
from .models import Agendamento
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

#INTERFACE WEB
def home(request):
    return render(request, 'home.html')

def login_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('novo_agendamento')  
        else:
            return render(request, 'login.html', {
                'erro': 'Usuário ou senha inválidos'
            })

    return render(request, 'login.html')

@login_required
def detalhes_agendamento(request, id):
    agendamento = get_object_or_404(
        Agendamento,
        id=id,
        cliente=request.user
    )

    if request.method == 'POST':
        agendamento.status = 'cancelado'
        agendamento.save()

        return redirect('meus_agendamentos')

    return render(request, 'detalhes_agendamento.html', {
        'agendamento': agendamento
    })

@login_required
def meus_agendamentos(request):
    meus_agendamentos = Agendamento.objects.filter(cliente=request.user)

    return render(request, 'meus_agendamentos.html', {
        'meus_agendamentos': meus_agendamentos
    })

@login_required
def novo_agendamento(request):
    servicos = Servico.objects.all()

    if request.method == 'POST':
        servico_id = request.POST.get('servico')
        data = request.POST.get('data')
        hora = request.POST.get('hora')

        data_hora = datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M")

        Agendamento.objects.create(
            cliente=request.user,
            servico_id=servico_id,
            data_hora=data_hora
        )

        messages.success(request, 'Agendado com sucesso!')

        return render(request, 'agendamento_sucesso.html')

    return render(request, 'novo_agendamento.html', {
        'servicos': servicos
    })

def logout_view(request):
    logout(request)
    return redirect('login')
    
#API
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def api_agendamentos(request):

    if request.method == 'GET':
        agendamentos = Agendamento.objects.filter(cliente=request.user)
        serializer = AgendamentoSerializer(agendamentos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(cliente=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import get_object_or_404

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def api_agendamento_detail(request, id):

    agendamento = get_object_or_404(
        Agendamento,
        id=id,
        cliente=request.user
    )

    if request.method == 'GET':
        serializer = AgendamentoSerializer(agendamento)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AgendamentoSerializer(agendamento, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        agendamento.delete()
        return Response(status=204)