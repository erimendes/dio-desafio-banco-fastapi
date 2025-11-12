# 🏦 DIO - Desafio Banco FastAPI Async

API assíncrona desenvolvida com FastAPI e SQLAlchemy AsyncIO, utilizando JWT para autenticação e SQLite como banco de dados.
Este projeto implementa operações bancárias básicas, como cadastro de usuários, autenticação, criação de contas e movimentações financeiras.

⚙️ Configuração Inicial com Poetry

Certifique-se de ter o Poetry - instalado no seu ambiente.
```Bash
# Criar o projeto
poetry new dio-desafio-banco-fastapi
cd dio-desafio-banco-fastapi

# Adicionar dependências principais
poetry add fastapi uvicorn pydantic python-jose python-multipart passlib[bcrypt]
```

🗄️ Banco de Dados - SQLite (Assíncrono)

Instale as dependências para trabalhar com SQLAlchemy AsyncIO e SQLite:
```Bash
poetry add databases sqlalchemy aiosqlite
poetry add pydantic-settings
poetry add passlib[bcrypt] pyjwt
```
No Linux (Ubuntu/Debian), instale o SQLite localmente:
```Bash
sudo apt update
sudo apt install sqlite3
```
⚙️ Configuração do .env

Crie um arquivo chamado .env na raiz do projeto com as variáveis de ambiente necessárias:
```Bash
# .env
ENVIRONMENT="local"
APP_NAME=Banco FastAPI Async
DEBUG=True
SECRET_KEY=sua_chave_secreta_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Caminho do banco SQLite
DATABASE_URL=sqlite+aiosqlite:///./bank.db
```

# 🏦 API Bancária com FastAPI

Uma aplicação **FastAPI** para gerenciamento bancário, com autenticação JWT, operações de contas e movimentações financeiras.

---

## 📘 Documentação Interativa

Acesse os endpoints e explore a API diretamente pelo navegador:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔐 Funcionalidades

- 👤 Cadastro de usuários  
- 🔑 Geração e validação de **tokens JWT**  
- 🏦 Criação de **contas bancárias**  
- 👥 Cadastro de **clientes**  
- 💸 Movimentações de **débito e crédito**  

---

## 🧩 Tecnologias Utilizadas

| Tecnologia | Descrição |
|-------------|------------|
| 🐍 **Python 3.11+** | Linguagem principal do projeto |
| ⚡ **FastAPI** | Framework moderno e performático para APIs |
| 🗄️ **SQLite + SQLAlchemy AsyncIO** | Banco de dados leve com ORM assíncrono |
| 🔐 **JWT (python-jose)** | Autenticação e autorização segura |
| 🧱 **Poetry** | Gerenciador de dependências e empacotamento |

---

## 🚀 Como Executar o Projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Instale as dependências
poetry install

# Ative o ambiente virtual
poetry shell

# Execute a aplicação
poetry uvicorn app.main:app --reload
```

## 🧠 Próximos Passos
 Adicionar testes automatizados
 Criar documentação de rotas com exemplos
 Implementar integração com outros bancos

---

## 📄 Licença
Este projeto é distribuído sob a licença MIT.
Sinta-se livre para usar, modificar e contribuir. 💡

---

## 🛠️ Estrutura Completa do Projeto (FastAPI + MVC)
```Bash
dio-desafio-banco-fastapi/
├── app/
│   ├── api/
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── account.py
│   │   │   ├── auth.py
│   │   │   ├── client.py
│   │   │   ├── transaction.py
│   │   │   └── user.py
│   │   └── __init__.py
│   │
│   ├── core/
│   │   ├── security.py
│   │   ├── exceptions.py
│   │   └── config.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── database.py
│   │   └── tables/
│   │       ├── __init__.py
│   │       ├── account.py
│   │       ├── client.py
│   │       ├── transaction.py
│   │       └── user.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── auth.py
│   │   ├── client.py
│   │   ├── transaction.py
│   │   └── user.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── client.py
│   │   ├── transaction.py
│   │   └── user.py
│   │
│   ├── main.py
│   └── __init__.py
│
├── pyproject.toml
└── README.md
```

🤝 Contribuindo

Sinta-se à vontade para enviar issues ou pull requests.
Este projeto foi desenvolvido para o Desafio DIO - Banco FastAPI Async.