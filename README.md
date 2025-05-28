# Sistema de Reservas

Este é um projeto simples de uma API REST para gerenciamento de reservas, construído com Flask, SQLAlchemy e Flask-RESTx. Ele oferece funcionalidades para criação e manipulação de reservas, utilizando um banco de dados SQLite e arquitetura modular com Blueprints. A aplicação é containerizada com Docker.

## Tecnologias Utilizadas

Python 3.x
Flask 3.1.0
Flask-SQLAlchemy 3.1.1
flask-restx
SQLite
Docker

## Estrutura do Projeto

.
├── app.py                  # Ponto de entrada da aplicação Flask  
├── database.py             # Inicialização do SQLAlchemy  
├── routes/  
│   └── reserva_route.py    # Rotas relacionadas a reservas (não incluso aqui)  
├── requirements.txt        # Dependências do projeto  
├── Dockerfile              # Configuração Docker  
└── README.md               # Documentação do projeto

## Como Executar

Requisitos: Docker (recomendado) ou Python 3 instalado localmente.

### Executar com Docker
bash

docker build -t sistema-reservas .
docker run -p 5001:5001 sistema-reservas