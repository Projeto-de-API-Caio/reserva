from flask import Blueprint, request, jsonify
from models.reserva_model import Reserva
from database import db
from services.validador_escola import validar_turma, validar_aluno
from sqlalchemy import and_

routes = Blueprint("routes", __name__)

@routes.route("/reservas", methods=["POST"])
def criar_reserva():
    dados = request.json
    campos = ["turma_id", "aluno_id", "sala", "data", "hora_inicio", "hora_fim"]
    for campo in campos:
        if not dados.get(campo):
            return jsonify({"erro": f"Campo '{campo}' é obrigatório"}), 400

    if not validar_turma(dados["turma_id"]):
        return jsonify({"erro": "Turma não encontrada"}), 400

    if not validar_aluno(dados["aluno_id"]):
        return jsonify({"erro": "Aluno não encontrado"}), 400

    conflito = Reserva.query.filter_by(
        sala=dados["sala"],
        data=dados["data"]
    ).filter(
        and_(
            Reserva.hora_inicio < dados["hora_fim"],
            Reserva.hora_fim > dados["hora_inicio"]
        )
    ).first()

    if conflito:
        return jsonify({"erro": "Conflito de horário para esta sala"}), 409

    try:
        reserva = Reserva(**dados)
        db.session.add(reserva)
        db.session.commit()
        return jsonify({"mensagem": "Reserva criada com sucesso"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500