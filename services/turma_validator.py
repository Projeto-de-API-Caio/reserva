import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("ESCOLA_API_URL", "http://localhost:5000")

def validar_turma(turma_id):
    try:
        resp = requests.get(f"{BASE_URL}/api/turmas/{turma_id}")
        return resp.status_code == 200
    except requests.exceptions.RequestException:
        return False

def validar_aluno(aluno_id):
    try:
        resp = requests.get(f"{BASE_URL}/api/alunos/{aluno_id}")
        return resp.status_code == 200
    except requests.exceptions.RequestException:
        return False
