from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

dm = SQLAlchemy()

class HistoricoListas(db.Model):
    __tablename__ = 'historico_listas'

    id_lista = db.Column(db.Integer,primary_key=True)
    id_servicio = db.Column(db.String(20)primary_key=True)

    def json(self):
        return {
            'id_lista': self.id_lista,
            'id_servicio': self.id_servicio
        }


class HistoricoSesiones(db.Model):
    pass
