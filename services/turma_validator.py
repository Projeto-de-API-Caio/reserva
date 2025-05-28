import requests
from os import getenv
from dotenv import load_dotenv

load_dotenv()

ESCOLA_API_URL = getenv("ESCOLA_API_URL", "http://127.0.0.1:8000")

def validar_turma(turma_id):
    try:
        response = requests.get(f"{ESCOLA_API_URL}/turmas/{turma_id}")
        return response.status_code == 200
    except Exception:
        return False

def validar_aluno(aluno_id):
    try:
        response = requests.get(f"{ESCOLA_API_URL}/alunos/{aluno_id}")
        return response.status_code == 200
    except Exception:
        return False
