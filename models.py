from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.Integer,primary_key=True)
    correo = db.Column(db.String(320),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    sexo = db.Column(db.String(1))
    fecha_nacimiento = db.Column(db.Date)

    def json(self):
        return {
            'id_usuario': self.id_usuario,
            'correo': self.correo,
            'password': self.password,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'sexo': self.sexo,
            'fecha_nacimiento': self.fecha_nacimiento
        }

class Sesion(db.Model):
    __tablename__ = 'sesion'

    id_sesion = db.Column(db.Integer,primary_key=True)
    id_usuario = db.Column(db.Integer,db.ForeignKey('usuario.id_usuario'),nullable=False)
    fecha = db.Column(db.TIMESTAMP,nullable=False)

    usuarioS = db.relationship('Usuario',backref='usuarioS')

    def json(self):
        return {
            'id_sesion': self.id_sesion,
            'id_usuario': self.id_usuario,
            'fecha': self.fecha
        }

class PagVisitada(db.Model):
    __tablename__ = 'pag_visitada'

    id = db.Column(db.Integer,primary_key=True)
    id_sesion = db.Column(db.Integer,db.ForeignKey('sesion.id_sesion'),nullable=False)
    id_servicio = db.Column(db.String(20),db.ForeignKey('servicio.id_servicio'),nullable=False)
    tiempo = db.Column(db.Time,nullable=False)

    sesionP = db.relationship('Sesion',backref='sesionP')
    usuarioP = db.relationship('Usuario',backref='usuarioP')

    def json(self):
        return {
            'id': self.id,
            'id_sesion': self.id_sesion,
            'id_servicio': self.id_servicio,
            'tiempo': self.tiempo
        }

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

    id_servicio = db.Column(db.String(20),db.ForeignKey('servicio.id_servicio'),primary_key=True)

    servicioH = db.relationship('Servicio',backref='servicioH')

    def json(self):
        return {
            'id_servicio': self.id_servicio
        }

class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id_servicio = db.Column(db.String(20),db.ForeignKey('servicio.id_servicio'),primary_key=True)

    servicioR = db.relationship('Servicio',backref='servicioR')

    def json(self):
        return {
            'id_servicio': self.id_servicio
        }

class Atraccion(db.Model):
    __tablename__ = 'atraccion'

    id_servicio = db.Column(db.String(20),db.ForeignKey('servicio.id_servicio'),primary_key=True)

    servicioA = db.relationship('Servicio',backref='servicioA')

    def json(self):
        return {
            'id_servicio': self.id_servicio
        }