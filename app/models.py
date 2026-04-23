from django.db import models
from django.contrib.auth.models import AbstractUser
 
#Usuários 
class Usuario(AbstractUser):
    TIPO_CHOICES = [
        ('cliente', 'Cliente'),
        ('barbeiro', 'Barbeiro'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='cliente')
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.get_full_name()} ({self.tipo})'

#Serviços
class Servico(models.Model):
    nome = models.CharField(max_length=100)       
    duracao = models.IntegerField()               
    preco = models.DecimalField(max_digits=6, decimal_places=2)

#Agendamentos
class Agendamento(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
        
    class Status(models.TextChoices):
        PENDENTE = 'pendente', 'Pendente'
        CONFIRMADO = 'confirmado', 'Confirmado'
        CANCELADO = 'cancelado', 'Cancelado'

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDENTE
    )