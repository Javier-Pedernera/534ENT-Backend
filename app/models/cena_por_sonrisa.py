import uuid
from datetime import datetime
from app import db

class CenaPorUnaSonrisa(db.Model):
    __tablename__ = 'cena_por_una_sonrisa'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60), nullable=False)  # Campo para el nombre
    apellido = db.Column(db.String(60), nullable=False)  # Campo para el apellido
    direccion = db.Column(db.String(120))
    pais_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    cena_asistira = db.Column(db.String(50))
    tipo_comida = db.Column(db.String(50))
    cantidad_invitados = db.Column(db.Integer)
    nombres_acompanantes = db.Column(db.Text)
    detalles = db.Column(db.Text)
    email = db.Column(db.String(120), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    codigo_unico = db.Column(db.String(36), unique=True, default=lambda: str(uuid.uuid4()))

    pais = db.relationship('Country', backref='formularios')

    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'direccion': self.direccion,
            'pais': self.pais.serialize() if self.pais else None,
            'cena_asistira': self.cena_asistira,
            'tipo_comida': self.tipo_comida,
            'cantidad_invitados': self.cantidad_invitados,
            'nombres_acompanantes': self.nombres_acompanantes,
            'detalles': self.detalles,
            'email': self.email,
            'fecha_registro': self.fecha_registro.isoformat(),
            'codigo_unico': self.codigo_unico
        }
