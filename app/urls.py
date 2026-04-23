from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logado/', views.logado, name='logado'),
    path('meus_agendamentos/', views.meus_agendamentos, name='meus_agendamentos'),
    path('novo_agendamento/', views.novo_agendamento, name='novo_agendamento'),
]