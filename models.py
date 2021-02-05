from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Servicio(db.Model):
    __tablename__ = 'servicio'

    id_servicio = db.Column(db.String(20),primary_key=True)
    nombre = db.Column(db.String(200),nullable=False)
    url = db.Column(db.String(200),nullable=False)
    direccion = db.Column(db.String(200))
    ciudad = db.Column(db.String(50))
    descripcion = db.Column(db.String(500))
    valoracion = db.Column(db.String(50))
    num_valoracion = db.Column(db.String(50))
    url_mapa = db.Column(db.String(500))

    def json(self):
        return {
            'id_servicio': self.id_servicio,
            'nombre': self.nombre,
            'url': self.url,
            'direccion': self.direccion,
            'ciudad': self.ciudad,
            'descripcion': self.descripcion,
            'valoracion': self.valoracion,
            'num_valoracion': self.num_valoracion,
            'url_mapa': self.url_mapa
        }


class Hotel(db.Model):
    __tablename__ = 'hotel'

    id_servicio = db.Column(db.String(20),primary_key=True,ForeignKey(servicio.id_servicio))

    def json(self):
        return {
            'id_servicio': self.id_servicio
        }

class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id_servicio = db.Column(db.String(20),primary_key=True,ForeignKey(servicio.id_servicio))

    def json(self):
        return {
            'id_servicio': self.id_servicio
        }
        