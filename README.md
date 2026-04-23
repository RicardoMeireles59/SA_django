# 💈 Barbearia & Shop Bclub

Sistema de agendamento para barbearia desenvolvido com **Python + Django**.

O projeto permite que clientes realizem login, visualizem seus agendamentos, criem novos e acompanhem o status (pendente, confirmado, cancelado).

---

## 🚀 Funcionalidades

- 🔐 Autenticação de usuários (login/logout)
- 📅 Criação de agendamentos
- 📋 Listagem de agendamentos do usuário
- 🔍 Visualização de detalhes do agendamento
- ❌ Cancelamento de agendamentos
- 🌐 Interface web com templates Django
- 🔌 API REST (Django REST Framework)

---

## 🛠️ Tecnologias utilizadas

- Python 3.x
- Django
- Django REST Framework
- HTML + CSS

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git

cd seu-repositorio
```  
### 2. Crie um ambiente virtual

```bash
python -m venv venv
```  
Ative o ambiente:

Windows
```bash
venv\Scripts\activate
```  

Linux / Mac

```bash
source venv/bin/activate
```  

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```  
Caso não exista o requirements.txt, instale manualmente:
### 3. Instale as dependências
```bash
pip install django djangorestframework
``` 

### 4. Execute as migrações
```bash
python manage.py migrate
``` 

### 5. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```
### 6. Inicie o servidor
```bash
python manage.py runserver
```
## 🌐 Acesso ao Sistema
O sistema pode ser acessado localmente através dos links:

* **Aplicação Principal:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Painel Administrativo:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔌 API de Agendamentos
O sistema oferece uma API REST para gerenciamento dos serviços:

| Ação | Método | Endpoint |
| :--- | :--- | :--- |
| **Listar agendamentos** | `GET` | `/api/agendamentos/` |
| **Criar agendamento** | `POST` | `/api/agendamentos/` |
| **Ver Detalhes** | `GET` | `/api/agendamentos/<id>/` |
| **Atualizar** | `PUT` | `/api/agendamentos/<id>/` |
| **Deletar** | `DELETE` | `/api/agendamentos/<id>/` |

---

## 📁 Estrutura Básica
O projeto está organizado seguindo o padrão de arquitetura Django:

```text
app/
 ├── models.py       # Definição das tabelas do banco de dados
 ├── serializers.py  # Conversão de modelos para JSON (API)
 ├── views.py        # Lógica das páginas e da API
 ├── urls.py         # Rotas e caminhos do sistema
 ├── templates/      # Arquivos HTML (Layout e Páginas)
 └── static/         # Arquivos CSS, Imagens e Assets