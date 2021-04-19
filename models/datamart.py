from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HistoricoListas(db.Model):
    __tablename__ = 'historico_listas'
    __bind_key__ = 'dm_turismo'

    id_lista = db.Column(db.Integer,primary_key=True)
    id_servicio = db.Column(db.String(20),primary_key=True)

    def json(self):
        return {
            'id_lista': self.id_lista,
            'id_servicio': self.id_servicio
        }


class HistoricoSesiones(db.Model):
    __tablename__ = 'historico_sesiones'
    __bind_key__ = 'dm_turismo'

    id_sesion = db.Column(db.Integer,primary_key=True)
    id_servicio = db.Column(db.String(20),primary_key=True)
    id_usuario = db.Column(db.Integer,nullable=False)

    def json(self):
        return {
            'id_sesion': self.id_sesion,
            'id_servicio': self.id_servicio,
            'id_usuario': self.id_usuario
        }
