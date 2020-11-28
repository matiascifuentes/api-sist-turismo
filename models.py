from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hotel(db.Model):
    __tablename__ = 'hotel'

    nombre = db.Column(db.String(200),nullable=False)
    url = db.Column(db.String(200),primary_key=True)
    descripcion = db.Column(db.String(500))
    ciudad = db.Column(db.String(50))
    direccion = db.Column(db.String(200))
    num_valoracion = db.Column(db.String(50))
    valoracion = db.Column(db.String(50))
    url_mapa = db.Column(db.String(500))

    def json(self):
        return {
            'nombre': self.nombre,
            'url': self.url,
            'descripcion': self.descripcion,
            'ciudad': self.ciudad,
            'direccion': self.direccion,
            'num_valoracion': self.num_valoracion,
            'valoracion': self.valoracion,
            'url_mapa': self.url_mapa
        }

class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    nombre = db.Column(db.String(200),nullable=False)
    url = db.Column(db.String(200),primary_key=True)
    ciudad = db.Column(db.String(50))
    direccion = db.Column(db.String(200))
    num_valoracion = db.Column(db.String(50))
    valoracion = db.Column(db.String(50))
    telefono = db.Column(db.String(20))
    url_mapa = db.Column(db.String(500))

    def json(self):
        return {
            'nombre': self.nombre,
            'url': self.url,
            'ciudad': self.ciudad,
            'direccion': self.direccion,
            'num_valoracion': self.num_valoracion,
            'valoracion': self.valoracion,
            'telefono': self.telefono,
            'url_mapa': self.url_mapa
        }
        