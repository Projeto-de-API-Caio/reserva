from flask import Blueprint, jsonify, request
from models import reserva_model
from services.turma_validator import validar_turma


reserva_bp = Blueprint('reserva_bp', __name__)


@reserva_bp.route('/', methods=['GET'])
def listar_reservas():
    reservas = reserva_model.listar_reservas()
    return jsonify(reservas), 200


@reserva_bp.route('/', methods=['POST'])
def criar_reserva():
    dados = request.json
    
    if not validar_turma(dados.get('turma_id')):
        return jsonify({"erro": "Turma não encontrada"}), 400

    reserva, status = reserva_model.criar_reserva(dados)
    return jsonify(reserva), status

@reserva_bp.route('/<int:id_reserva>', methods=['GET'])
def obter_reserva(id_reserva):
    try:
        reserva = reserva_model.obter_reserva(id_reserva)
        return jsonify(reserva), 200
    except reserva_model.ReservaNotFound:
        return jsonify({'erro': 'Reserva não encontrada'}), 404

@reserva_bp.route('/<int:id_reserva>', methods=['DELETE'])
def excluir_reserva(id_reserva):
    try:
        reserva_model.excluir_reserva(id_reserva)
        return jsonify({"mensagem": "Reserva excluída com sucesso"}), 200
    except reserva_model.ReservaNotFound:
        return jsonify({'erro': 'Reserva não encontrada'}), 404