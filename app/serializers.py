from rest_framework import serializers
from .models import Agendamento, Servico

class ServicoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Servico
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Agendamento
        fields = '__all__'
        read_only_fields = ['cliente']