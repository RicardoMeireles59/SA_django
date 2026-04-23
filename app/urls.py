from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('meus_agendamentos/', views.meus_agendamentos, name='meus_agendamentos'),
    path('novo_agendamento/', views.novo_agendamento, name='novo_agendamento'),
    path('detalhes_agendamento/<int:id>/', views.detalhes_agendamento, name='detalhes_agendamento'),
    path('logout/', views.logout_view, name='logout'),
    path('api/agendamentos/', views.api_agendamentos),
    path('api/agendamentos/<int:id>/', views.api_agendamento_detail),
]

