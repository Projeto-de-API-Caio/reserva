from database import db
from datetime import datetime

class ReservaNotFound():
    pass

class Reserva(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    turma_id = db.Column(db.Integer, nullable=False)
    sala = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.String(10), nullable=False)
    hora_fim = db.Column(db.String(10), nullable=False)

    def __init__(self, turma_id, sala, data, hora_inicio, hora_fim):
        self.turma_id = turma_id
        self.sala = sala
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim


    def to_dict(self):
        return {
            "id": self.id,
            "turma_id": self.turma_id,
            "sala": self.sala,
            "data": self.data,
            "hora_inicio": self.hora_inicio,
            "hora_fim": self.hora_fim,
            "criado_em": self.criado_em.isoformat() if self.criado_em else None
        }
    
def obter_reserva(id_reserva):
    reservas = Reserva.query.all()
    print(reservas)
    return [reserva.to_dict() for reserva in reservas], 200
    
def criar_reserva(dados):
    try:
        turma_id=dados['turma_id'],
        sala=dados['sala'],
        data=datetime.fromisoformat(dados['data']).date(),
        hora_inicio=dados['hora_inicio'],
        hora_fim=dados['hora_fim']

        reserva = Reserva(turma_id, sala, data, hora_inicio, hora_fim)

        db.session.add(reserva)
        db.session.commit()

        return obter_reserva(reserva.id), 201
    except Exception as e:
        db.session.rollback()
        return {"erro": 'Reserva indisponível'}, 400
    
def excluir_reserva(id_reserva):
    reserva = Reserva.query.get(id_reserva)
    if not reserva:
        raise ReservaNotFound()
    db.session.delete(reserva)
    db.session.commit()